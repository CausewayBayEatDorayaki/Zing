import glob
import os

import pandas
from PySide2.QtCore import QFileInfo

from component.parse_ltl import ParseLtl
from component.state import StateSpace
from dao.zing_dao import ZingDao
from dao.zipc_dao import ZipcDao
import re


class ZingService:
    def __init__(self):
        self.zipcDao = ZipcDao()
        self.zingDao = ZingDao()
        self.stateSpace = None
        self.praseLtl = None

    # ************************************************************************************
    # ************************************ Zipc Model ************************************
    # ************************************************************************************

    # zipc_model
    def get_model(self, fileName):
        fileinfo = QFileInfo(fileName);
        # 获取绝对路径
        file_path = fileinfo.absolutePath();
        file_list = glob.glob(os.path.join(file_path, '*.stm'))  # 读取文件夹中所有后缀为stm的文件地址
        file_name_list = []
        for file in file_list:
            temp_fileinfo = QFileInfo(file);
            file_name = temp_fileinfo.fileName()
            file_name_list.append(file_name)

        return self.zipcDao.get_model_map(file_list, file_name_list)

    def print_list_model(self, map):
        for item in map:
            i = 0;
            for model in map[item]:
                if (i == 0):
                    str = item + '事件'
                    i += 1
                elif (i == 1):
                    str = item + '状态'
                    i += 1
                else:
                    str = item + '动作'
                    i += 1
                print('\n===============================' + str + '===============================\n')
                for esa in model:
                    print(esa)

    def print_table_model(self, model_map):
        pandas.set_option('display.max_rows', None)
        pandas.set_option('display.max_columns', 500)
        pandas.set_option('display.width', 5000)
        for mmp in model_map:
            print(model_map[mmp])

    def list_transfer_table(self, model_map):
        for mmp in model_map:
            data = []
            tempdata = []
            i = 0
            for item in model_map[mmp][2]:
                # print(i)
                if (i != len(model_map[mmp][1])):
                    tempdata.append(item)
                    i += 1
                else:
                    data.append(tempdata)
                    tempdata = []
                    tempdata.append(item)
                    i = 1;
            data.append(tempdata)

            model_map[mmp] = pandas.DataFrame(data, index=model_map[mmp][0], columns=model_map[mmp][1])

        return model_map

    # ************************************************************************************
    # ************************************ Zing Model ************************************
    # ************************************************************************************

    def get_file_dital(self, fileName, suffix):
        fileinfo = QFileInfo(fileName);
        # 获取绝对路径
        file_path = fileinfo.absolutePath();
        file_list = glob.glob(os.path.join(file_path, suffix))  # 读取文件夹中所有后缀为stm的文件地址
        file_name_list = []
        for file in file_list:
            temp_fileinfo = QFileInfo(file);
            file_name = temp_fileinfo.fileName()
            file_name_list.append(file_name)
        return [file_list, file_name_list]

    def get_model_dfs(self, fileName):
        file_dital = self.get_file_dital(fileName, '*.stm')
        return self.zingDao.load_stm_file(file_dital[0], file_dital[1])

    def get_var_text(self, fileName):
        file_dital = self.get_file_dital(fileName, '*.var')
        return self.zingDao.load_var_file(file_dital[0][0])

    def get_model_var(self, fileName):
        file_dital = self.get_file_dital(fileName, '*.var')
        return self.zingDao.load_var_file_list(file_dital[0][0])

    def get_model_var_map(self, fileName):
        file_dital = self.get_file_dital(fileName, '*.var')
        var_list = self.zingDao.load_var_file_list(file_dital[0][0])
        print(var_list)
        var_file = self.zingDao.load_var_file1(file_dital[0][0])
        map = {}
        code = ''
        for item in var_list:
            items = item.split('=')
            code = code + '\nmap[\'' + items[0] + '\']=' + items[0]
        # print(var_file+code)
        exec(var_file + code)
        print(map)
        return map

    def check_int(self, value):
        return str(value).isdigit()

    def check_bool(self, value):
        flag = True
        if value == 'True' or value == 'False':
            flag = True
        else:
            flag = False
        return flag

    # 括号匹配
    def check_brackets(self, value):
        SYMBOLS = {'}': '{', ']': '[', ')': '('}
        SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()
        arr = []
        for c in value:
            # print('arr', arr)
            if c in SYMBOLS_L:
                arr.append(c)
            elif c in SYMBOLS_R:
                if arr[len(arr) - 1] == SYMBOLS[c]:
                    arr.pop()
                else:
                    return False
        if not arr:
            return True
        return False

    def check_var(self, value, var_map):
        value = value.replace('[G]', ' ')
        value = value.replace('[F]', ' ')
        value = value.replace('[W]', ' ')
        value = value.replace('[U]', ' ')
        value = value.replace('[R]', ' ')
        value = value.replace('[X]', ' ')
        value1 = value.replace('{', ' ')
        value1 = value1.replace('}', ' ')
        value1 = value1.replace('(', ' ')
        value1 = value1.replace(')', ' ')
        value1 = value1.replace('==', ' ')
        value1 = value1.replace('!=', ' ')
        value1 = value1.replace('>=', ' ')
        value1 = value1.replace('<=', ' ')
        value1 = value1.replace('>', ' ')
        value1 = value1.replace('<', ' ')
        value1 = value1.replace('&', ' ')
        value1 = value1.replace('|', ' ')
        remain_list = value1.split(' ')
        # print(remain_list, 'remain_list')
        # 变量名是否在导入的数据中
        for i in remain_list:
            if i.isdigit() or i == 'True' or i == 'False' or i == '' or i in var_map:
                continue
            else:
                print(i, '<-----return False in Phase4 checking LTL')
                return False
        return True

    def check_ltl(self, value, var_map):
        if value == 'DeadLock':
            return True
        if value == 'Unreachable':
            return True
        value = value.replace(' ', '')  # 去空格
        # 检查括号
        if not self.check_brackets(value):
            return False
        # 变量检查
        if not self.check_var(value, var_map):
            return False
        return True

    # def check_ltl(self, value, var_map):
    #     return True
    #     value = value.replace(' ', '')  # 去空格
    #     if value[0:3] == '[G]' or value[0:3] == '[F]' or value[0:3] == '[X]':
    #         value = value[3:]
    #     print(value)
    #     value = value.replace('[G]', ' ')
    #     value = value.replace('[F]', ' ')
    #     value = value.replace('[W]', ' ')
    #     value = value.replace('[U]', ' ')
    #     value = value.replace('[R]', ' ')
    #     value = value.replace('[X]', ' ')
    #     value1 = value.replace('⇒', ' ')
    #     value2 = value1.replace('(', ' ')
    #     value2 = value2.replace(')', ' ')
    #     value2 = value2.replace('==', ' ')
    #     value2 = value2.replace('!=', ' ')
    #     value2 = value2.replace('>=', ' ')
    #     value2 = value2.replace('<=', ' ')
    #     value2 = value2.replace('>', ' ')
    #     value2 = value2.replace('<', ' ')
    #     value2 = value2.replace('&', ' ')
    #     value2 = value2.replace('|', ' ')
    #     list = value2.split(' ')
    #     list1 = value1.split(' ')
    #     print(list1, 'list1')
    #     print(list, 'list')
    #
    #     # 变量名是否在导入的数据中
    #     for i in list:
    #         if i.isdigit() or i == 'True' or i == 'False':
    #             continue
    #         if i in var_map:
    #             for j in range(0, len(list1)):
    #                 # 将逻辑变量名替换为变量值
    #                 list1[j] = list1[j].replace(i, str(var_map[i]))
    #         else:
    #             print(i, '<-----return False in Phase4 checking LTL')
    #             return False
    #     # print(list1,'list1')
    #     # list1去掉了LTL语法的一阶逻辑，将逻辑变量名替换为变量值执行检查
    #     # for i in list1:
    #     #     print(i)
    #     #     try:
    #     #         exec(i)
    #     #     except Exception as error:
    #     #         print(error,'error')
    #     return True

    def get_dfs_format(self, prj_path):
        dfs = {}
        file_dital = self.get_file_dital(prj_path, '*.stm')
        for i in range(0, len(file_dital[0])):
            dfs[file_dital[1][i]] = self.zingDao.load_stm_file_format(file_dital[0][i])
        return dfs

    def get_BMC_state_transition_tree(self, prj_path, var_map, deep):
        dfs = self.get_dfs_format(prj_path)
        self.stateSpace = StateSpace(dfs, var_map)
        tree = self.stateSpace.get_BMC_state_space_tree(deep)
        return tree

    def get_simple_state_transition_tree(self, prj_path, var_map):
        dfs = self.get_dfs_format(prj_path)
        self.stateSpace = StateSpace(dfs, var_map)
        tree = self.stateSpace.get_simple_state_space_tree()
        return tree

    def get_state_transition_tree(self, prj_path, var_map):
        dfs = self.get_dfs_format(prj_path)
        self.stateSpace = StateSpace(dfs, var_map)
        tree = self.stateSpace.get_state_space_tree()
        return tree

    def check_dead_lock(self, tree, dfs):
        events_lsit = []
        for dfk in dfs:
            row = list(dfs[dfk]['Unnamed: 0'].values)
            events_lsit.extend(row)
        for node in tree.leaves():
            smap = eval(node.identifier.split('-')[2])
            # 检查忽略单元格是否是死锁状态
            if node.tag[0] == '/':
                count = 0
                for key in events_lsit:
                    if smap[key] == True:
                        count += 1
                if count <= 1:
                    branch = []
                    for id in tree.rsearch(node.identifier):
                        branch.append(id)
                    branch.reverse()
                    return branch
            # 因为X / R三种情况叶子节点都会标注，只有event都为False，才会不进入状态空间重复检查而返回。
            # 也就是说叶子节点只要没有被标记就是进入了死锁状态
            elif node.tag[0] != 'X' and node.tag[0] != 'R' and node.tag[0] != 'B':
                branch = []
                for id in tree.rsearch(node.identifier):
                    branch.append(id)
                branch.reverse()
                return branch

                # count = 0
                # for key in events_lsit:
                #     if smap[key] == True:
                #         count += 1
                # if count == 1:
                #     branch = []
                #     for id in tree.rsearch(node.identifier):
                #         branch.append(id)
                #     branch.reverse()
                #     return branch

        #     for events in events_lsit:
        #         dlflg = True
        #         for event in events:
        #             if smap[event]==True:
        #                 dlflg=False
        #                 break
        #         if dlflg:
        #             print(111)
        # print(tree.link_past_node(node.identifier))

    def check_unreachable(self, tree):
        for node in tree.leaves():
            if node.tag[0] == 'X':
                branch = []
                for id in tree.rsearch(node.identifier):
                    branch.append(id)
                branch.reverse()
                return branch

    def check_model(self, ltl, tree, dfs):
        if ltl == 'DeadLock':
            return self.check_dead_lock(tree, dfs)
        elif ltl == 'Unreachable':
            return self.check_unreachable(tree)
        self.praseLtl = ParseLtl(tree)
        result = self.praseLtl.check_ltl_entry(ltl)
        return result

    def rebuilt_df_item(code, parent_state):
        key_list = list(parent_state.keys())
        value_list = list(parent_state.values())
        state_space_str = ''
        for item in key_list:
            state_space_str = state_space_str + item + '=' + str(parent_state[item]) + '\n'
        state_space_str = state_space_str + '\n' + code

        for item in key_list:
            state_space_str = state_space_str + '\nparent_state[\'' + item + '\']=' + item

        print(state_space_str)

    def calculation_compression_rate(self, tree, depth):
        leaves = tree.leaves()
        rbps_num = tree.all_nodes().__len__()
        purning_num = 0
        for leaf in leaves:
            if leaf.tag[0] == 'R':
                tdp = tree.depth(leaf)
                # print(tdp)
                # tag = leaf.tag.split('(')[0][10:]
                purning_num += depth - tdp
        bmc_num = rbps_num + purning_num
        compression_rate = rbps_num / bmc_num
        return [str(rbps_num), str(bmc_num), str(compression_rate)]


if __name__ == '__main__':
    service = ZingService()

    # var_map = {'DLL_CE_SOC': False, 'DLL_CE_PREQ': False, 'DLL_CE_PRES': False, 'DLL_CE_SOA': False,
    #            'DLL_CE_ASND': False, 'DLL_CE_SOC_TIMEOUT': False, 'DLL_CT11_1': False, 'DLL_CE_RESET': False,
    #            'DLL_ME_PRES': False, 'DLL_ME_PRES_TIMEOUT': False, 'DLL_ME_ASND': False, 'xDLL_ME_SOC_TRIG': True,
    #            'DLL_ME_OP_RESET': False, 'DLL_CEV_LOSS_SOC': False, 'DLL_CEV_LOSS_SOA': False,
    #            'DLL_CEV_LOSS_PREQ': False, 'DLL_CEV_CYCLE_EXCEED': False, 'DLL_MEV_LOSS_PRES': False, 'SoAProcess': 1,
    #            'presProcess': 0, 'asndProcess': 0, 'sendToNMT': 0, 'isochr': 1, 'isochr_out': 1, 'async_in': 1,
    #            'async_out': 1, 'error': 0, 'multiplexed_1': 1, 'NMT_CST_1': 3, 'SoAAuthorization': 0,
    #            'DLL_MS_CAN_OP': 1, 'flag': 0, 'presNum': 0, 'count': 0,'CS_STATE':1,'DLL_MS_OPERATIONAL_STATE':0}

    # path = '../model_example/powerlink_v8.0/powerlink.zpf'
    # map = service.get_model(path)
    # service.print_list_model(map)
    # path = '../model_example/Powerlink_simplify/Powerlink_simplify.zprj'
    path = '../model_example/tcpip_handshake/tcpip_handshake.zprj'
    map = service.get_model_dfs(path)
    var_map = service.get_model_var_map(path)
    tree = service.get_state_transition_tree(path, var_map)
    service.calculation_compression_rate(tree, 10)
    # tree = service.get_full_state_transition_tree(path,var_map)
    # print(tree)
    # nodes = tree.leaves()
    # print(nodes)
    # print("{'root':0}" in tree.rsearch(nodes[0].identifier))
    # for i in tree.rsearch(nodes[0].identifier):
    #     print(i)
    # service.check_dead_lock(tree,map)
