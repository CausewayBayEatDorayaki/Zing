import pandas
from pandas import DataFrame


class ZingDao:
    def __init__(self):
        pass

    def load_var_file(self, project_path):
        file = open(project_path, 'r', encoding='utf-8')
        text = file.read()
        file.close()
        return text
    def load_var_file1(self, project_path):
        file = open(project_path, 'r', encoding='utf-8')
        list = file.readlines()
        list = ''.join(list).strip('\n')
        file.close()
        return list

    def load_var_file_list(self, project_path):
        file = open(project_path, 'r', encoding='utf-8')
        list = file.readlines()
        # list = ''.join(list).strip('\n')
        file.close()
        rlist = []
        for item in list:
            item = item.strip()
            if item == '' or item[0] == '#':
                pass
            else:
                rlist.append(item.strip())
        return rlist

    def load_stm_file(self, file_list, file_name_list):
        dfs = {}
        for i in range(len(file_list)):
            dfs[file_name_list[i]] = pandas.read_csv(file_list[i])
        return dfs

    def load_stm_file_format(self,full_path):
        rdf = pandas.read_csv(full_path)
        list_col_str = rdf.columns.values
        col = list_col_str[1:]
        row = rdf['Unnamed: 0'].values
        #print(col)
        data={}
        for i in col:
            data[i]=list(rdf[i])
        df = DataFrame(data, index=row)
        #print(df.loc['E_POWERON'].loc['S_POWEROFF'])
        return df



if __name__ == '__main__':
    zingDao = ZingDao()
    #txt = zingDao.load_var_file_list('../model_example/Modbus/Modbus.var')
    #txt = zingDao.load_var_file_list('../model_example/Powerlink/Powerlink.var')
    zingDao.load_stm_file_format('../model_example/musicplayer/musicplayer.stm')
