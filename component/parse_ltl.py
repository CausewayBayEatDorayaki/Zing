import re


# from service.zing_service import ZingService


class ParseLtl:
    def __init__(self, tree):
        self.tree = tree
        self.branch = []
        self.Node = None
        self.counter_flag = True
        self.state_key = list(self.tree.get_node('--{\'root\':0}').data.keys())
        self.param_str_list = []
        self.param_str_map = {}

    #  & | != == > >= < <= () G F X U R W ¬
    def deal_list_GFX(self, symbol, i, ltl_ist):
        # ltl_ist[i] = 'self.zing_solver_?'
        count = 1
        for j in range(i + 2, len(ltl_ist)):
            if ltl_ist[j] == '(BRCH,i,' or ltl_ist[j] == '(':
                count += 1
            elif ltl_ist[j] == ')':
                count -= 1
            if count == 0:
                # print(i, j)
                ltl_ist[j] = ')'
                self.param_str_list.append([ltl_ist[i], ''.join(ltl_ist[i + 2:j])])
                break

    def deal_list_U(self, symbol, i, ltl_ist):
        # ltl_ist[i] = 'self.zing_solver_?'
        for j in range(i, len(ltl_ist)):
            if ltl_ist[j] == ')':
                # U_str = ''.join(ltl_ist[i + 2:j])
                # self.param_str_list.append([ltl_ist[i], U_str.split(',')])
                self.param_str_list.append([ltl_ist[i], ''.join(ltl_ist[i + 2:j])])
                break

    def deal_GFX(self, symbol, i, phi):
        phi[i] = 'self.zing_solver_' + symbol
        phi[i + 1] = '(BRCH,i,'
        count = 1
        for j in range(i, len(phi)):
            if phi[j] == '{':
                count += 1
            elif phi[j] == '}':
                count -= 1
            if count == 0:
                phi[j] = ')'
                break

    def deal_U(self, symbol, i, phi):
        phi[i - 2] = 'self.zing_solver_' + symbol
        temp = phi[i - 1]
        phi[i - 1] = '(BRCH,i,'
        phi[i] = temp + '?'
        phi[i + 2] = ')'

    def format_formula(self, phi):
        # print(phi)
        phi = phi.replace(' ', '')
        phi = phi.replace('[G]', '@')
        phi = phi.replace('[F]', '#')
        phi = phi.replace('[X]', '$')
        phi = phi.replace('[U]', '?')
        spp = re.split(r"([@#$?{}])", phi)
        phi_list = []
        for i in range(0, len(spp)):
            if spp[i] != '':
                if spp[i] == '@':
                    phi_list.append('[G]')
                elif spp[i] == '#':
                    phi_list.append('[F]')
                elif spp[i] == '$':
                    phi_list.append('[X]')
                elif spp[i] == '?':
                    phi_list.append('[U]')
                else:
                    phi_list.append(spp[i])
        for i in range(0, len(phi_list)):
            if (phi_list[i] == '[G]'):
                self.deal_GFX('G', i, phi_list)
            elif (phi_list[i] == '[F]'):
                self.deal_GFX('F', i, phi_list)
            elif (phi_list[i] == '[X]'):
                self.deal_GFX('X', i, phi_list)
            elif (phi_list[i] == '[U]'):
                self.deal_U('U', i, phi_list)

        for i in range(0, len(phi_list)):
            for key in self.state_key:
                phi_list[i] = phi_list[i].replace('||', ' or ')
                phi_list[i] = phi_list[i].replace('|', ' or ')
                phi_list[i] = phi_list[i].replace('&&', ' and ')
                phi_list[i] = phi_list[i].replace('&', ' and ')
                if key in phi_list[i]:
                    phi_list[i] = phi_list[i].replace(key, 'smap[\'' + key + '\']')
        phi_str = ''
        for item in phi_list:
            phi_str += item

        return [phi_list, phi_str]

    # G后面只能接变量、括号、[
    # def zing_solver_G(self, branch, i, phi):
    #     if phi == True:
    #         if i < len(branch)-1:
    #             i += 1
    #             tmp = self.tree.get_node(branch[i]).identifier
    #             smap = eval(tmp)
    #             #exec_str = 'smap=' + str(smap) + '\n'
    #             flag = True
    #             exec_str = 'flag=' + self.G_str
    #             print('Exec_G_flag: ', exec_str)
    #             exec(exec_str)
    #             if flag:
    #                 return self.zing_solver_G(branch, i, True)
    #             else:
    #                 return False
    #     else:
    #         return False
    #     return True
    #
    # def zing_solver_F(self, branch, i, phi):
    #     if phi == False:
    #         if i < len(branch)-1:
    #             i += 1
    #             tmp = self.tree.get_node(branch[i]).identifier
    #             smap = eval(tmp)
    #             flag = True
    #             exec_str = 'flag=' + self.F_str
    #             print('Exec_F_flag: ', exec_str)
    #             exec(exec_str)
    #             if flag:
    #                 return True
    #             else:
    #                 return self.zing_solver_F(branch, i, False)
    #         else:
    #             return False
    #     return True
    #
    # def zing_solver_X(self, branch, i, phi):
    #     if i < len(branch)-1:
    #         i += 1
    #         tmp = self.tree.get_node(branch[i]).identifier
    #         smap = eval(tmp)
    #         flag = True
    #         exec_str = 'flag=' + self.X_str
    #         print('Exec_X_flag: ', exec_str)
    #         exec(exec_str)
    #         if flag:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    #
    # def zing_solver_U(self, branch, i, p, q):
    #     if p:
    #         if i < len(branch)-1:
    #             i += 1
    #             tmp = self.tree.get_node(branch[i]).identifier
    #             smap = eval(tmp)
    #             flag_q = True
    #             flag_p = True
    #             exec_str = 'flag_q=' + self.U_str[1] + '\nflag_p=' + self.U_str[0]
    #             print('Exec_X_flag: ', exec_str)
    #             exec(exec_str)
    #             if flag_q:
    #                 return True
    #             else:
    #                 return self.zing_solver_U(branch, i, flag_p, flag_q)
    #         else:
    #             return False
    #     else:
    #         if i < len(branch):
    #             i += 1
    #             tmp = self.tree.get_node(branch[i]).identifier
    #             smap = eval(tmp)
    #             flag_q = True
    #             flag_p = True
    #             exec_str = 'flag_q=' + self.U_str[1] + '\nflag_p=' + self.U_str[0]
    #             print('Exec_X_flag: ', exec_str)
    #             exec(exec_str)
    #             return self.zing_solver_U(branch, i, flag_p, flag_q)
    #         else:
    #             return False

    def zing_solver_formula(self, ltl):
        ptl = self.tree.paths_to_leaves()
        # print(ptl)
        for branch in ptl:

            self.branch = branch
            # print(branch)
            # branch : identifier list
            brch = branch[1].split('-')[2]  # 第一个状态空间
            smap = eval(brch)
            # 判断嵌套。。。需要优化
            if len(ltl) > 17 and ltl[17] == 'G':
                for i in range(1, len(branch)):
                    smap = eval(branch[i].split('-')[2])
                    # print(smap)
                    if not self.check_ltl(ltl, smap, branch, i):
                        return branch
            # 判断嵌套。。。需要优化
            elif len(ltl) > 17 and ltl[17] == 'F':
                for i in range(1, len(branch)):
                    smap = eval(branch[i].split('-')[2])
                    # print(smap)
                    if self.check_ltl(ltl, smap, branch, i):
                        return None
            else:
                if not self.check_ltl(ltl, smap, branch, 1):
                    return branch
        return None

    def set_str_param(self, ltl_list):
        for i in range(0, len(ltl_list)):
            if (ltl_list[i] == 'self.zing_solver_G'):
                self.deal_list_GFX('G', i, ltl_list)
            elif (ltl_list[i] == 'self.zing_solver_F'):
                self.deal_list_GFX('F', i, ltl_list)
            elif (ltl_list[i] == 'self.zing_solver_X'):
                self.deal_list_GFX('X', i, ltl_list)
            elif (ltl_list[i] == 'self.zing_solver_U'):
                self.deal_list_U('U', i, ltl_list)
        # print('self.param_list:::', self.param_str_list)
        # print(self.G_str, 'str_G')
        # print(self.F_str, 'str_F')
        # print(self.U_str, 'str_U')

    def zing_solver_G(self, BRCH, i, phi):
        for j in range(i, len(BRCH)):
            smap = eval(BRCH[j].split('-')[2])
            flag = True
            loc = locals()
            estr = 'flag=(' + str(phi) + ')'
            exec(estr)
            flag = loc['flag']
            if not flag:
                return False
        return True

    def zing_solver_F(self, BRCH, i, phi):
        loop = True
        for j in range(i, len(BRCH)):
            smap = eval(BRCH[j].split('-')[2])
            # print(smap)
            flag = False
            loc = locals()
            estr = 'flag=(' + str(phi) + ')'
            exec(estr)
            flag = loc['flag']
            if flag == True:
                return True
            if j == len(BRCH) - 1 and loop and BRCH[j].split('-')[0][0] != '/' and BRCH[j].split('-')[0][0] != 'X' and \
                    BRCH[j].split('-')[0][0] != 'S' and not ('B' in BRCH[j].split('-')[0]):
                j = int(BRCH[j].split('-')[0].split('R')[0])
                loop = False
        return False

    def zing_solver_X(self, BRCH, i, phi):
        if i < len(BRCH) - 1:
            i += 1
            smap = eval(BRCH[i].split('-')[2])
            flag = False
            loc = locals()
            estr = 'flag=(' + str(phi) + ')'
            exec(estr)
            flag = loc['flag']
            return flag
        return False

    def zing_solver_U(self, BRCH, i, phi):
        pq = phi.split('?')
        flag = False
        loop = True
        for j in range(i, len(BRCH)):
            p = True
            q = True
            smap = eval(BRCH[i].split('-')[2])
            loc = locals()
            estr = 'p=' + pq[0] + '\nq=' + pq[1]
            exec(estr)
            p = loc['p']
            q = loc['q']
            if p:
                flag = True
                if q:
                    return True
            else:
                if q and flag:
                    return True
                return False
            if j == len(BRCH) - 1 and loop and BRCH[j].split('-')[0] != '/' and BRCH[j].split('-')[0] != 'X':
                j = int(BRCH[j].split('-')[0].split('R')[0])
                loop = False
        return False

    def check_ltl(self, ltl, smap, BRCH, i):
        # print('ltl:::',ltl)
        # print('param_list:::',self.param_str_list)
        local_param_str_list = self.param_str_list
        for j in range(len(self.param_str_list) - 1, -1, -1):
            e_str = local_param_str_list[j][0] + '(BRCH,i,\"' + local_param_str_list[j][1] + '\")'
            torf = True
            e_str = 'torf=' + e_str
            loc = locals()
            exec(e_str)
            torf = loc['torf']
            # print('TorF', torf)
            o_str = local_param_str_list[j][0] + '(BRCH,i,' + local_param_str_list[j][1] + ')'
            # print(o_str)
            # print(ltl)
            ltl = ltl.replace(o_str, str(torf))
            if ltl == 'True':
                return True
            elif ltl == 'False':
                return False
            for k in range(0, j):
                # print('pre:::',local_param_str_list[k][1])
                local_param_str_list[k][1] = local_param_str_list[k][1].replace(o_str, str(torf))
                # print('aft:::', local_param_str_list[k][1])

        # print('filal ltl:::',ltl)
        estr = 'isltlt=' + ltl
        loc = locals()
        exec(estr)
        isltlt = loc['isltlt']
        return isltlt

    def check_ltl_entry(self, ltl_str):
        ltl = self.format_formula(ltl_str)
        # ltl[0]为list ltl[1]为str
        self.set_str_param(ltl[0])
        return self.zing_solver_formula(ltl[1])

# if __name__ == '__main__':
#     service = ZingService()
#     tree = service.get_state_transition_tree('../model_example/Powerlink_simplify/Powerlink_simplify.zprj')
#     pl = ParseLtl(tree)
#     ltl ='[F]{DLL_CE_SOC==False}'#
#     print('result', pl.check_ltl_entry(ltl))
