import sys
from treelib import Tree, Node

sys.setrecursionlimit(1000000000)

state_space = {}
var_text = ''


class StateSpace:
    count = 0

    def __init__(self, df, state_map, var_txt):
        self.df = df
        self.state_list = df.columns.values
        self.event_list = df.index.values

        self.key_list = list(state_map.keys())
        self.tree = Tree()
        self.var_text = var_txt
        self.state_space = state_map

    def init_necessary_var(self):
        global state_space
        state_space_str = ''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key
        state_space_str = state_space_str + '\n' + self.var_text
        exec(state_space_str)
        state_space = self.state_space
        state_space['ZING_STATE'] = 0

    def JUMP(self, index):
        self.state_space['ZING_STATE'] = index
        state_space_str=''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key
        for item in self.key_list:
            state_space_str = state_space_str + '\nself.state_space[\'' + item + '\']=' + item
        exec(state_space_str)
        # print(state_space)

    def rebuilt_df_item(self, parent_state):
        state_space_str = ''
        for key in self.key_list:
            state_space_str = state_space_str + '\nglobal ' + key
        for item in self.key_list:
            state_space_str = state_space_str + '\n' + item + '=' + str(parent_state[item]) + '\n'
        # print(state_space_str)
        exec(state_space_str)

    def exec_item_code(self, code):
        # print(code)
        state_space_str = ''
        if code == '/' or code == 'X':
            pass
        else:
            for key in self.key_list:
                state_space_str = state_space_str + '\nglobal ' + key
            state_space_str = state_space_str + '\n' + code
            state_space_str = state_space_str.replace('JUMP(', 'self.JUMP(')

        exec(state_space_str)

    #   now_state_space: map存储的状态空间
    #   pnode: 父节点id（map状态空间的values()）
    #   root: 树根
    def JUMP_RECURSION(self, pnode, root, now_state_space):
        for event in self.event_list:
            # print(now_state_space.values(),'pre')
            now_state_space[event] = True
            ssv = str(now_state_space.values())
            # 储存Node
            # 判断当前状态空间是否重复
            if root.contains(ssv):
                now_state_space[event] = False
                return
            # 状态空间不重复创建Node
            node = Node(tag='('+event+','+self.state_list[now_state_space['ZING_STATE']]+')', identifier=ssv, data=now_state_space)
            root.add_node(node, parent=pnode)

            # exec()将now_state_space赋值给全局变量state_space在进行递归
            self.rebuilt_df_item(now_state_space)
            self.state_space = now_state_space
            # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
            self.exec_item_code(self.df.loc[event].loc[self.state_list[self.state_space['ZING_STATE']]])
            self.state_space[event] = False  # 当前状态置为False,执行code传递下一状态进行递归
            # print(self.state_space.values(),'state_space\n')
            self.JUMP_RECURSION(ssv, root, state_space)

    def get_state_space_tree(self):
        self.init_necessary_var()
        init_state_space = str(self.state_space.values())
        self.tree.create_node(tag='(-1, 0)', identifier=init_state_space, data=self.state_space)
        self.JUMP_RECURSION(init_state_space, self.tree, self.state_space)
        self.tree.show()
