import os
from PySide2.QtCore import QFileInfo

from dao.zing_dao import ZingDao
import pandas


def write_file(prj_path, msg):
    file = open(prj_path, 'w', encoding='utf-8')
    file.write(msg)
    file.close()


class ModelDesignerService:
    def __init__(self):
        self.zingDao = ZingDao()

    def delete_file(self, project_path, filename):
        full_path = project_path + '/' + filename
        if os.path.exists(full_path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(full_path)
            # os.unlink(path)
        else:
            print('no such file:%s' % full_path)

    def load_var_file(self, project_path, filename):
        full_path = project_path + '/' + filename
        file = open(full_path, 'r', encoding='utf-8')
        text = file.read()
        file.close()
        return text

    def load_var_file_list(self, project_path, filename):
        full_path = project_path + '/' + filename
        file = open(full_path, 'r', encoding='utf-8')
        list = file.readlines()
        list = ''.join(list).strip('\n')
        file.close()
        return list

    def load_stm_file_format(self,full_path):
        df_data=self.load_stm_file(full_path)
        df=pandas.DataFrame()
        # ...

    def load_stm_file(self, full_path):
        df = pandas.read_csv(full_path)
        list_col_str = df.columns.values
        col = list_col_str[1:]
        row = df['Unnamed: 0'].values
        return [row, col, df]

    def create_stm_file(self, path, filename, df):
        full_path = path + '/' + filename
        write_file(full_path, '')
        df.to_csv(full_path)

    def save_var_file(self, path, filename, text):
        full_path = path + '/' + filename
        write_file(full_path, text)

    def save_stm_files(self, path, filenames, dfs):
        for item in filenames:
            dfs[item].to_csv(path + '/' + item)
        print("save", path, filenames, dfs)

    def designer_get_model_path(self, fileName):
        fileinfo = QFileInfo(fileName);
        # 获取绝对路径
        file_path = fileinfo.absolutePath();
        return file_path

    def create_project(self, prj_path, prj_name):
        os.makedirs(prj_path)
        var_file_path = prj_path + '/' + prj_name + '.var'
        zp_file_path = prj_path + '/' + prj_name + '.zprj'
        write_file(var_file_path, '# 请将STSM中的全部变量定义在此文件中并附上初始值。\n'
                                  '# 变量命名限制：不允许出现子串，如已定义x_Play再定义x_Play_1是不被允许的,x_Play_0,x_Play_1是允许的。\n'
                                  '# 外部事件：模型检查时外部事件自动触发，外部事命名需要在变量前加x_，如x_Poweroff=False。\n'
                                  '# 事件变量：需要全部赋Bool值如有外部事件为x_Play，需定义为：x_Play=True。\n'
                                  '# 状态变量：需要以固定方式赋值：如文件Music.stm内状态变量需定义为：Music_STATE=0,其中Music为文件名0为状态初始值。\n')
        write_file(zp_file_path, '#zprj file')


if __name__ == '__main__':
    service = ModelDesignerService()
    txt = service.load_var_file_list('D:/User/Abb/Project/ModelChecker/Mc/model_example/zingprj', 'tcpip_handshake.var')
    txt = txt.splitlines()
    print(txt)
    # df = service.load_stm_file('../abb.stm')
    # df = df[2]
    # # df=df[df.columns.values[1:]]
    # print(df)
    # list_col_str = df.columns.values
    # col = list_col_str[1:]
    # row = df['a'].values
    # print(row)
    # print(col)
    # print(service.load_stm_file(['../model_example/zingprj/stm_name1.stm']))
