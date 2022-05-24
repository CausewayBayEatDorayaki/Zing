import xml.etree.cElementTree as ET
import xml.etree.ElementTree as ET


class ZipcDao:
    def __init__(self):
        pass

    # model_map:    key:'file_name.stm'
    #               value:[event_list,state_list,action_list]
    def get_model_map(self,file_path_list,file_name_list):
        model_map={}
        i=0
        for fn in file_name_list:
            model_map[fn]=self.get_stm_data(file_path_list[i])
            i += 1
        return model_map

    def get_stm_data(self,path):
        tree = ET.parse(path)
        root = tree.getroot()
        state = root.find('EVENT')
        event = root.find('STATE')
        action = root.find('ACTION')

        event_list = []
        state_list = []
        action_list = []
        self.get_tail(event, event_list)
        self.get_tail(state, state_list)
        self.get_action(action, action_list)

        model=[event_list,state_list,action_list]
        return model


    def get_tail(self,root,list):
        for child in root:
            if (child.tag == 'STRING_WORD_DATA'):
                try:
                    child.attrib['String']
                except (KeyError, IOError):
                    print("key error")
                else:
                    list.append(child.attrib['String'])
                #print(child.attrib['String'])
            if (child.attrib.__contains__('MarkType')):
                list.append(child.attrib['MarkType'])
            self.get_tail(child, list)

    def get_action(self,action,action_list):
        for child in action:
            if (child.tag == 'STM_ACTION_CELL'):
                tmplist = []
                self.get_tail(child, tmplist)
                action_list.append(tmplist)

if __name__ == '__main__':
    tree = ET.parse('../model_example/MusicPlayer_zipc/Music.stm')
    tree = ET.parse('../model_example/modbus_v1.0/a.stm')
    root = tree.getroot()
    event_list = []
    state_list = []
    action_list = []
    state = root.find('EVENT')
    event = root.find('STATE')
    action = root.find('ACTION')
    dao=ZipcDao()
    dao.get_tail(event,event_list)
    dao.get_tail(state,state_list)
    dao.get_action(action,action_list)
    print(event_list,state_list,action_list)

# <EVENT/>事件
#   </EVENT_CELL>
#       </EVENT_STRING>
#           </ZIPC_STRING_MANAGER>
#               </STRING_LINE_DATA>
#                   <STRING_WORD_DATA String="power"/>
# <STATE/>状态
# <ACTION>动作
# <STM_AC_PARENT/>赋值
# <STM_TR_PARENT/>跳转
# </ACTION>

# <ACTION>
#     <STM_ACTION_CELL ENum="0" SNum="0">
#       <STM_TR_PARENT>
#         <ROOT_ACTION_DATA/>
#         <MY_ACTION_DATA VerticalNum="2" HorizontalNum="1"/>
#         <STM_AC_CHILD>
#           <ROOT_ACTION_DATA/>
#           <ACTION_STRING>
#             <ZIPC_STRING_MANAGER>
#               <STRING_LINE_DATA>
#                 <STRING_WORD_DATA String="play=false;"/>

#<STM_ACTION_CELL ENum="1" SNum="1">
#   <STM_CELL_AC>
#       <ROOT_ACTION_DATA MarkType="1"/>
#   </STM_CELL_AC>
#</STM_ACTION_CELL>
#Ignore:  MarkType="1"
#Impossible: MarkType="2"


# </ZIPC_PROJECT_FILE>
#     <Simulator/>
#         <STM_CloneFile0>.\DLL_CS.stm</STM_CloneFile0>
#         <STM_CloneFile1>.\DLL_MS_OPERATIONAL.stm</STM_CloneFile1>