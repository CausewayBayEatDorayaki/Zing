import sys
from treelib import Tree, Node

from service.zing_service import ZingService

sys.setrecursionlimit(100000000)
from dao.zing_dao import ZingDao

path='../model_example/Powerlink/'

dao = ZingDao()
zing_service=ZingService()
var_text = dao.load_var_file(path + 'Powerlink.var')
df = dao.load_stm_file_format(path+'DLL_MS_OPERATIONAL.stm')
state_list = df.columns.values
event_list = df.index.values
state_space = zing_service.get_model_var_map(path + 'Powerlink.zprj')
state_space['ZING_STATE']=0
init_state_space = str(state_space.values())
all_state_space = [init_state_space]
key_list = list(state_space.keys())

exec(var_text)

def init_state_var():
    pass

def JUMP(index):
    state_space_str = 'ZING_STATE=' + str(index)
    for item in key_list:
        state_space_str = state_space_str + '\nstate_space[\'' + item + '\']=' + item
    exec(state_space_str)
    # print(state_space)


def rebuilt_df_item(parent_state):
    state_space_str = ''
    for item in key_list:
        state_space_str = state_space_str + item + '=' + str(parent_state[item]) + '\n'

    # print(state_space_str)
    exec(state_space_str)


def exec_item_code(code):
    #print(code)
    state_space_str = ''
    if code == '/' or code == 'X':
        pass
    else:
        state_space_str = state_space_str + '\n' + code
    exec(state_space_str)


# rebuilt_df_item(df.loc['E_POWERON'].loc['S_POWEROFF'], state_space)
def search_tree(pnode):
    str_t = ''
    for i in range(0, pnode.deep):
        str_t = str_t + '\t'
    str_t=str_t+str(pnode.deep)+str(pnode.status_space.values())
    print(str_t)
    for i in range(len(pnode.child)):
        search_tree(pnode.child[i])

# def JUMP_RECURSION(pnode, now_state_space):
#     for event in event_list:
#         print(now_state_space.values(),'pre')
#         # 判断当前状态空间是否重复
#         now_state_space[event] = True
#         ssv = str(now_state_space.values())
#         for i in all_state_space:
#             if i == ssv:
#                 now_state_space[event]=False
#                 return
#         all_state_space.append(ssv)
#         print('assv',all_state_space)
#         node = StateNode()
#         # exec()记录当前状态空间到Node
#         rebuilt_df_item(now_state_space)
#         node.set_node_state_space(state_space)
#         node.set_node_deep(pnode.deep + 1)
#         pnode.set_child(node)
#         print(node.status_space.values(), 'node???')
#
#         # 状态不重复执行单元格code进行递归
#         state_space[event] = False  # 当前状态置为False,执行code传递下一状态进行递归
#         # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态
#         exec_item_code(df.loc[event].loc[state_list[state_space['ZING_STATE']]])
#
#         print(state_space.values(),'state_space\n||||||||||||||||||||||||||||||||')
#         JUMP_RECURSION(node, state_space)


#   now_state_space: map存储的状态空间
#   pnode: 父节点id（map状态空间的values()）
#   root: 树根
def JUMP_RECURSION(pnode, root, now_state_space):
    for event in event_list:
        #print(now_state_space.values(),'pre')
        now_state_space[event] = True
        ssv = str(now_state_space.values())
        # 储存Node
        # 判断当前状态空间是否重复
        if tree.contains(ssv):
            now_state_space[event] = False
            return
        # 状态空间不重复创建Node
        node = Node(tag=ssv, identifier=ssv, data=now_state_space)
        root.add_node(node, parent=pnode)

        # exec()将now_state_space赋值给全局变量state_space在进行递归
        rebuilt_df_item(now_state_space)
        # exec单元格代码，如果有JUMP函数就会改变state_space的ZING_STATE状态,exec_item_code只可改变外面全局变量state_space值
        exec_item_code(df.loc[event].loc[state_list[state_space['ZING_STATE']]])
        state_space[event] = False  # 当前状态置为False,执行code传递下一状态进行递归
        #print(state_space.values(),'state_space\n')
        JUMP_RECURSION(ssv, root,state_space)

def get_state_space_tree(self):
    self.init_necessary_var()
    print(self.state_space)
    init_state_space = str(self.state_space.values())
    self.tree.create_node(tag=init_state_space, identifier=init_state_space, data=self.state_space)

    self.JUMP_RECURSION(init_state_space, self.tree, self.state_space)
    self.tree.show()

tree=Tree()
tree.create_node(tag=init_state_space, identifier=init_state_space, data=state_space)
JUMP_RECURSION(init_state_space,tree,state_space)
tree.show()
