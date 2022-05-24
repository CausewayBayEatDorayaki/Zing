import sys
import time
import itertools

from treelib import Tree, Node

sys.setrecursionlimit(1000000000)


class StateSpace:
    count = 0

    def __init__(self, dfs, state_map):
        self.dfs = dfs
        self.df = None
        self.df_stm_name_key = list(dfs.keys())  # dfs的key值也就是stm的表名
        # self.state_list = df.columns.values
        # self.event_list = df.index.values
        self.state_list = []
        self.event_list = []  # 内外部事件的名称
        self.external_event_list = []
        self.org_state = state_map
        self.state_space = state_map
        self.key_list = list(state_map.keys())  # 状态空间key
        self.tree = Tree()
        # self.var_text = var_txt

    def init_necessary_var(self):
        self.state_space = self.org_state
        state_space_str = ''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key + '\n' + key + '=' + str(self.state_space[key])

        # state_space_str = state_space_str + '\n' + self.var_text
        exec(state_space_str)

        # for key in self.df_stm_name_key:
        #     self.state_space[key.split('.')[0] + '_STATE'] = 0

        elst = []
        for df in self.dfs:
            elst.extend(list(self.dfs[df].index.values))
        self.event_list = elst

        for item in self.event_list:
            if item[0] == 'x':
                self.external_event_list.append(item)

    def rebuilt_df_item(self, parent_state):
        state_space_str = ''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key
        for item in self.key_list:
            state_space_str = state_space_str + '\n' + item + '=' + str(parent_state[item])
        # print(state_space_str)
        exec(state_space_str)

    # def exec_item_code(self, code, df_name, now_state_space):
    #     # print(code)
    #     loc_state_space={}
    #     state_space_str = ''
    #     if code == '/' or code == 'X':
    #         return now_state_space
    #     else:
    #         for key in self.key_list:
    #             state_space_str = state_space_str + '\nglobal ' + key
    #         state_space_str = state_space_str + '\n' + code
    #         state_space_str = state_space_str.replace('JUMP(', 'loc_state_space=self.JUMP(\'' + df_name + '\',')
    #     print(state_space_str)
    #     loc=locals()
    #     exec(state_space_str)
    #     loc_state_space=loc['loc_state_space']
    #     print('exec',loc_state_space)
    #     return loc_state_space
    # def JUMP(self, df_name, index):
    #
    #     state_space_str = ''
    #     loc_state_space={}
    #     for key in self.key_list:
    #         state_space_str = state_space_str + '\nglobal ' + key
    #     for item in self.key_list:
    #         state_space_str = state_space_str + '\nloc_state_space[\'' + item + '\']=' + item
    #     loc = locals()
    #     exec(state_space_str)
    #     loc_state_space=loc['loc_state_space']
    #     loc_state_space[df_name.split('.')[0] + '_STATE'] = index
    #
    #     print('JUMP', loc_state_space)
    #     return loc_state_space
    #     # print(state_space)
    # def JUMP_RECURSION(self, pnode, root, now_state_space):
    #     for event in self.event_list:
    #         if self.state_space[event] == True:
    #             ssv = str(now_state_space)
    #             # flag=False
    #             # for i in root.rsearch(pnode):
    #             #     if ssv==i:  # 判断当前状态空间是否重复
    #             #         flag=True
    #             #         break
    #             # if flag:
    #             #     continue
    #             if root.contains(ssv):
    #                 return
    #
    #             print(now_state_space)
    #
    #             df_name = self.judge_df(event)  # 获取df key
    #             self.df = self.dfs[df_name]
    #             self.state_list = list(self.df.columns.values)
    #             node = Node(
    #                 tag='(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ') - ' + ssv,
    #                 identifier=ssv, data=df_name)
    #             root.add_node(node, parent=pnode)
    #             # exec()将now_state_space赋值给全局变量state_space在进行递归
    #             self.rebuilt_df_item(now_state_space)
    #             # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
    #             new_space_state=self.exec_item_code(
    #                 self.df.loc[event].loc[self.state_list[now_state_space[df_name.split('.')[0] + '_STATE']]],
    #                 df_name,now_state_space)
    #             self.JUMP_RECURSION(ssv, root, new_space_state)

    def judge_df(self, event):
        for key in self.df_stm_name_key:
            for item in self.dfs[key].index.values:
                if event == item:
                    return key
        return 'error event string!'

    def exec_item_code(self, code, df_name):
        # print(code)
        state_space_str = ''
        if code == '/' or code == 'X':
            return code
        else:
            for key in self.key_list:
                state_space_str = state_space_str + '\nglobal ' + key
            state_space_str = state_space_str + '\n' + code
            if 'JUMP(' in code:
                state_space_str = state_space_str.replace('JUMP(', 'self.JUMP(\'' + df_name + '\',')
            else:
                for item in self.key_list:
                    state_space_str = state_space_str + '\nself.state_space[\'' + item + '\']=' + item
        # print(':::Server',state_space_str)
        exec(state_space_str)
        return None

    def JUMP(self, df_name, index):
        state_space_str = ''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key
        for item in self.key_list:
            state_space_str = state_space_str + '\nself.state_space[\'' + item + '\']=' + item
        exec(state_space_str)
        self.state_space[df_name.split('.')[0] + '_STATE'] = index
        # print('JUMP', self.state_space)
        # print(state_space)

    # pnode: 父节点id（map状态空间的values()） - string
    # now_state_space: map存储的状态空间 - map
    # root: 树根 - Tree()
    # identifier结构:[S树节点个数]-(x,y)-{状态空间}
    # tag结构：[/ | X | Repeat](x,y)(x,y)-{状态空间}
    def JUMP_RECURSION_SIMPLE(self, pnode, root, now_state_space):
        for event in self.event_list:
            # print(event)
            if self.state_space[event]:
                self.state_space = now_state_space
                df_name = self.judge_df(event)  # 获取df key
                ssv = '(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(
                    now_state_space)
                if root.contains('-' + ssv):
                    releaf = root.get_node('-' + ssv)
                    node = Node(tag='Repeat' + releaf.tag,
                                identifier='S' + str(root.__len__() + 1) + '-' + ssv, data=df_name)
                    root.add_node(node, parent=pnode)
                    continue
                # 状态空间不重复
                self.df = self.dfs[df_name]
                self.state_list = list(self.df.columns.values)
                node = Node(tag=ssv, identifier='-' + ssv, data=df_name)
                root.add_node(node, parent=pnode)
                # exec()将now_state_space赋值给全局变量state_space在进行递归
                self.rebuilt_df_item(now_state_space)
                # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
                isEcode = self.exec_item_code(
                    self.df.loc[event].loc[self.state_list[self.state_space[df_name.split('.')[0] + '_STATE']]],
                    df_name)
                if isEcode != None:
                    lssv = isEcode + '<-(' + event + ',' + str(
                        self.state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(self.state_space)
                    if root.contains(lssv):
                        continue
                    node1 = Node(tag=lssv, identifier=lssv, data=df_name)
                    root.add_node(node1, parent='-' + ssv)
                    continue
                self.JUMP_RECURSION_SIMPLE('-' + ssv, root, self.state_space)

    # pnode: 父节点id（map状态空间的values()） - string
    # now_state_space: map存储的状态空间 - map
    # root: 树根 - Tree()
    # identifier结构:[重复深度数字R]树节点个数-(x,y)-{状态空间}
    # tag结构：[/ | X | Repeat重复深度数字](x,y)-{状态空间}
    def JUMP_RECURSION(self, pnode, root, now_state_space):
        for event in self.event_list:
            # print(event)
            if self.state_space[event]:
                self.state_space = now_state_space
                df_name = self.judge_df(event)  # 获取df key
                ssv = '(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(
                    now_state_space)
                self.df = self.dfs[df_name]
                self.state_list = list(self.df.columns.values)
                idf = str(root.__len__() + 1) + '-' + ssv
                flag = False
                for i in root.rsearch(pnode):
                    if ssv == i.split('-')[1] + '-' + i.split('-')[2]:  # 判断当前状态空间是否重复
                        releaf = root.get_node(i)
                        node = Node(tag='RepeatDeep' + str(root.depth(releaf)) + releaf.tag,
                                    identifier=str(root.depth(releaf)) + 'R' + idf, data=df_name)
                        root.add_node(node, parent=pnode)
                        flag = True
                        break
                if flag:  # 当前branch状态空间不重复
                    continue

                node = Node(tag=ssv, identifier=idf, data=df_name)
                root.add_node(node, parent=pnode)
                # exec()将now_state_space赋值给全局变量state_space在进行递归
                self.rebuilt_df_item(now_state_space)
                # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
                isEcode = self.exec_item_code(
                    self.df.loc[event].loc[self.state_list[self.state_space[df_name.split('.')[0] + '_STATE']]],
                    df_name)
                if isEcode is not None:
                    lssv = isEcode + '(' + event + ',' + str(
                        self.state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(self.state_space)
                    flag = False
                    for i in root.rsearch(idf):
                        if lssv == i.split('-')[1] + '-' + i.split('-')[2]:  # 判断当前状态空间是否重复
                            flag = True
                            break
                    if flag:
                        continue
                    cid = str(root.__len__() + 1) + '-' + lssv
                    node1 = Node(tag=lssv, identifier=cid, data=df_name)
                    root.add_node(node1, parent=idf)
                    continue

                self.JUMP_RECURSION(idf, root, self.state_space)

    # pnode: 父节点id（map状态空间的values()） - string
    # now_state_space: map存储的状态空间 - map
    # root: 树根 - Tree()
    # identifier结构:[重复深度数字R|BMC深度数字B]树节点个数-(x,y)-{状态空间}
    # tag结构：[/ | X | BMC深度数字 | Repeat重复深度数字](x,y)-{状态空间}
    def JUMP_BMC_RECURSION(self, pnode, root, now_state_space):
        for event in self.event_list:
            # print(event)
            if self.state_space[event]:
                self.state_space = now_state_space
                df_name = self.judge_df(event)  # 获取df key
                ssv = '(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(
                    now_state_space)
                self.df = self.dfs[df_name]
                self.state_list = list(self.df.columns.values)
                idf = str(root.__len__() + 1) + '-' + ssv

                if root.depth(root.get_node(pnode)) == self.bmc:
                    node = Node(tag='BMC' + str(self.bmc) + ssv, identifier=str(self.bmc) + 'B' + idf, data=df_name)
                    root.add_node(node, parent=pnode)
                    continue

                flag = False
                for i in root.rsearch(pnode):
                    if ssv == i.split('-')[1] + '-' + i.split('-')[2]:  # 判断当前状态空间是否重复
                        releaf = root.get_node(i)
                        node = Node(tag='RepeatDeep' + str(root.depth(releaf)) + releaf.tag,
                                    identifier=str(root.depth(releaf)) + 'R' + idf, data=df_name)
                        root.add_node(node, parent=pnode)
                        flag = True
                        break
                if flag:  # 当前branch状态空间不重复
                    continue

                node = Node(tag=ssv, identifier=idf, data=df_name)
                root.add_node(node, parent=pnode)
                # exec()将now_state_space赋值给全局变量state_space在进行递归
                self.rebuilt_df_item(now_state_space)
                # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
                isEcode = self.exec_item_code(
                    self.df.loc[event].loc[self.state_list[self.state_space[df_name.split('.')[0] + '_STATE']]],
                    df_name)
                if isEcode is not None:
                    lssv = isEcode + '(' + event + ',' + str(
                        self.state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(self.state_space)
                    flag = False
                    for i in root.rsearch(idf):
                        if lssv == i.split('-')[1] + '-' + i.split('-')[2]:  # 判断当前状态空间是否重复
                            flag = True
                            break
                    if flag:
                        continue
                    cid = str(root.__len__() + 1) + '-' + lssv
                    node1 = Node(tag=lssv, identifier=cid, data=df_name)
                    root.add_node(node1, parent=idf)
                    continue

                self.JUMP_BMC_RECURSION(idf, root, self.state_space)

    def JUMP_RECURSION_FULL(self, pnode, root, now_state_space):
        for event in self.event_list:
            now_state_space[event] = True
            self.state_space = now_state_space
            df_name = self.judge_df(event)  # 获取df key
            ssv = '(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ')-' + str(
                now_state_space)
            # 储存Node
            # 判断当前状态空间是否重复
            if root.contains(ssv):
                now_state_space[event] = False
                return
            # 状态空间不重复

            self.df = self.dfs[df_name]
            self.state_list = list(self.df.columns.values)

            node = Node(tag=ssv, identifier=ssv, data=df_name)
            root.add_node(node, parent=pnode)
            # exec()将now_state_space赋值给全局变量state_space在进行递归
            self.rebuilt_df_item(now_state_space)
            # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
            isDorE = self.exec_item_code(
                self.df.loc[event].loc[self.state_list[self.state_space[df_name.split('.')[0] + '_STATE']]],
                df_name)
            if isDorE is not None:
                lssv = '(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ') -> ' + isDorE
                if root.contains(str(lssv)):
                    return
                node1 = Node(
                    tag=lssv,
                    identifier=lssv, data=df_name)
                root.add_node(node1, parent=ssv)
                return
            now_state_space[event] = False
            self.JUMP_RECURSION_FULL(ssv, root, self.state_space)

    # def JUMP_RECURSION_FULL(self, pnode, root, now_state_space):
    #     for event in self.event_list:
    #         now_state_space[event] = True
    #         self.state_space = now_state_space
    #         ssv = str(now_state_space)
    #         # 储存Node
    #         # 判断当前状态空间是否重复
    #         if root.contains(ssv):
    #             now_state_space[event] = False
    #             return
    #         # 状态空间不重复
    #         df_name = self.judge_df(event)  # 获取df key
    #         self.df = self.dfs[df_name]
    #         self.state_list = list(self.df.columns.values)
    #
    #         node = Node(tag='(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ') - ' + ssv,
    #                     identifier=ssv, data=df_name)
    #         root.add_node(node, parent=pnode)
    #         # exec()将now_state_space赋值给全局变量state_space在进行递归
    #         self.rebuilt_df_item(now_state_space)
    #         # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
    #         isDorE=self.exec_item_code(
    #             self.df.loc[event].loc[self.state_list[self.state_space[df_name.split('.')[0] + '_STATE']]],
    #             df_name)
    #         if isDorE != None:
    #             lssv='(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ') -> ' + isDorE
    #             if root.contains(str(lssv)):
    #                 return
    #             node1 = Node(
    #                 tag='(' + event + ',' + str(now_state_space[df_name.split('.')[0] + '_STATE']) + ') -> ' + isDorE,
    #                 identifier=lssv, data=df_name)
    #             root.add_node(node1, parent=ssv)
    #             return
    #         now_state_space[event] = False
    #         self.JUMP_RECURSION_FULL(ssv, root, self.state_space)

    # 状态初始化组合
    def pmt_state(self):
        tuplist = []
        for i in self.df_stm_name_key:
            tmplist = []
            for j in range(0, len(list(self.dfs[i].columns.values))):
                # self.state_space[self.df_stm_name_key.split('.')[0] + '_STATE'] = j
                tmplist.append(j)
            tuplist.append(tuple(tmplist))
        all_state_tup = ''
        estr = 'all_state_tup=itertools.product(' + str(tuplist).replace('[', '').replace(']', '') + ')'
        loc = locals()
        exec(estr)
        all_state_tup = loc['all_state_tup']
        return all_state_tup

    def get_state_space_tree(self):
        self.init_necessary_var()
        self.tree.create_node(tag='root', identifier='--{\'root\':0}', data=self.state_space)
        if self.external_event_list:
            for ex_event in self.external_event_list:
                self.state_space[ex_event] = True
                self.JUMP_RECURSION('--{\'root\':0}', self.tree, self.state_space)
        else:
            self.JUMP_RECURSION('--{\'root\':0}', self.tree, self.state_space)
        # self.tree.show()
        return self.tree

    def get_BMC_state_space_tree(self, deep):
        self.bmc = deep
        self.init_necessary_var()
        self.tree.create_node(tag='root', identifier='--{\'root\':0}', data=self.state_space)
        self.JUMP_BMC_RECURSION('--{\'root\':0}', self.tree, self.state_space)
        return self.tree

    def get_simple_state_space_tree(self):
        self.init_necessary_var()
        self.tree.create_node(tag='root', identifier='--{\'root\':0}', data=self.state_space)
        if self.external_event_list:
            for ex_event in self.external_event_list:
                self.state_space[ex_event] = True
                self.JUMP_RECURSION('--{\'root\':0}', self.tree, self.state_space)
        else:
            self.JUMP_RECURSION('--{\'root\':0}', self.tree, self.state_space)
        # self.tree.show()
        return self.tree

    def get_full_state_space_tree(self):
        self.init_necessary_var()
        self.tree.create_node(tag='root', identifier='{\'root\':0}', data=self.state_space)
        for ex_event in self.external_event_list:
            self.state_space[ex_event] = True
            self.JUMP_RECURSION_FULL('{\'root\':0}', self.tree, self.state_space)
        self.tree.show()
        return self.tree
