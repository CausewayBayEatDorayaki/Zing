import psutil
from treelib import Tree, Node

if __name__ == '__main__':
    # exe_code_test()
    p = psutil.Process(31432)
    min = p.memory_full_info().uss / 1024
    # pmt='\n input:'
    max=0
    while(True):
        mem_info_end = p.memory_full_info().uss / 1024
        if mem_info_end>max:
            max=mem_info_end
        print('end:::',max-min)
    # print('start:::',mem_info_start)
    #113500 118872
    #3300.0 12928
