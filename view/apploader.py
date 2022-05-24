import os
import sys
import time
import threading
import psutil
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtGui import QIcon, QColor, QKeySequence, QTextCharFormat, QBrush, QMovie
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

from component.load_singal import LoadSignal, CheckerSignal
from view.model_designer import ModelDesigner
from service.zing_service import ZingService


class MainWindow:
    def __init__(self):
        self.signal = LoadSignal()
        self.signal.Signal.connect(self.checker)
        self.checker_signal = CheckerSignal()
        self.checker_signal.Signal.connect(self.show_result)
        self.tree = None
        self.prj_path = ''
        self.global_var_map = {}
        self.service = ZingService()
        self.dfs = {}
        self.var = []
        self.phase = [False, False, False]
        self.branch = {}
        self.mem_max = 0
        self.mem_now = 0
        # frame4初始显示
        self.frame = 4
        # 从文件中动态加载UI定义,创建一个相应的窗口对象。 注意：里面的控件对象也成为窗口对象的属性了 比如 self.ui.button , self.ui.textEdit

        self.ui = QUiLoader().load('../ui/main_ui.ui')
        self.ui.setWindowIcon(QIcon('../img/zing.png'))
        self.add_ltl_ui = QUiLoader().load('../ui/add_ltl.ui')
        self.add_ltl_ui.setWindowIcon(QIcon('../img/zing.png'))
        self.wait_gif = QMovie('../img/load.gif')
        self.model_designer = ModelDesigner()

        self.ui.actionopen.triggered.connect(self.open_file_button)
        self.ui.actiondesign.triggered.connect(self.design_button)
        self.ui.actionclose.triggered.connect(self.action_close)
        self.ui.actionabout.triggered.connect(self.action_about)
        self.ui.actionhelp.triggered.connect(self.action_help)
        self.ui.pushButton_open.clicked.connect(self.open_file_button)
        self.ui.pushButton_design.clicked.connect(self.design_button)
        self.ui.pushButton_add.clicked.connect(self.add_button)
        self.ui.pushButton_delete.clicked.connect(self.delete_button)
        self.ui.pushButton_previous.clicked.connect(self.previous_button)
        self.ui.pushButton_next.clicked.connect(self.next_button)
        self.ui.toolButton.clicked.connect(self.tree_show_tips)

        self.add_ltl_ui.pushButton_0.clicked.connect(self.add_ltl_X)
        self.add_ltl_ui.pushButton_1.clicked.connect(self.add_ltl_G)
        self.add_ltl_ui.pushButton_2.clicked.connect(self.add_ltl_F)
        self.add_ltl_ui.pushButton_3.clicked.connect(self.add_ltl_W)
        self.add_ltl_ui.pushButton_4.clicked.connect(self.add_ltl_U)
        self.add_ltl_ui.pushButton_5.clicked.connect(self.add_ltl_R)
        self.add_ltl_ui.pushButton_6.clicked.connect(self.add_ltl_left_bracket)
        self.add_ltl_ui.pushButton_7.clicked.connect(self.add_ltl_right_bracket)
        self.add_ltl_ui.pushButton_8.clicked.connect(self.add_ltl_equal)
        self.add_ltl_ui.pushButton_9.clicked.connect(self.add_ltl_not_equal)
        self.add_ltl_ui.pushButton_10.clicked.connect(self.add_ltl_greater)
        self.add_ltl_ui.pushButton_11.clicked.connect(self.add_ltl_less)
        self.add_ltl_ui.pushButton_12.clicked.connect(self.add_ltl_greater_and_equal)
        self.add_ltl_ui.pushButton_13.clicked.connect(self.add_ltl_less_and_equal)
        self.add_ltl_ui.pushButton_14.clicked.connect(self.add_ltl_and)
        self.add_ltl_ui.pushButton_15.clicked.connect(self.add_ltl_or)
        self.add_ltl_ui.pushButton_16.clicked.connect(self.add_ltl_imply)
        self.add_ltl_ui.pushButton_17.clicked.connect(self.add_ltl_cancel)
        self.add_ltl_ui.pushButton_18.clicked.connect(self.add_ltl_confirm)
        self.add_ltl_ui.listWidget.itemDoubleClicked.connect(self.list_double_clicked)

        # 模型案例菜单
        self.ui.actionPowerlink.triggered.connect(self.action_powerlink)
        self.ui.actionModbus.triggered.connect(self.action_modbus)
        self.ui.actionTcp_ip.triggered.connect(self.actionTcp_ip)

        # 加入Ctrl+D打开案例
        self.shortcut = QShortcut(QKeySequence("Ctrl+T"), self.ui)
        self.shortcut.activated.connect(self.actionTcp_ip)
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self.ui)
        self.shortcut.activated.connect(self.action_powerlink)

        self.ui.treeWidget_2.doubleClicked.connect(self.show_branch)
        self.ui.treeWidget_3.doubleClicked.connect(self.linkage)

    # 模型案例菜单 ——> powerlink
    def action_powerlink(self):
        prj_path = '../model_example/Powerlink_simplify/Powerlink_simplify.zprj'
        self.set_phase1_data(prj_path)

    # 模型案例菜单 ——> modbus
    def action_modbus(self):
        prj_path = '../model_example/Modbus/Modbus.zprj'
        self.set_phase1_data(prj_path)

    # 模型案例菜单 ——> tcp/ip
    def actionTcp_ip(self):
        prj_path = '../model_example/tcpip_handshake_boom/tcpip_handshake_boom.zprj'
        self.set_phase1_data(prj_path)

    # 帮助菜单 ——> 使用说明
    def action_help(self):
        QMessageBox.about(self.ui, '.:: Instructions ::.',
                          '~~~ZING Model Checker~~~\n\n'
                          'Model checking has four phases：\n'
                          'In phase 1, importe model into the verification tool.\n\n'
                          'In phase 2, set the initial value of the model\n\n'
                          'In phase 3, using LTL (linear time temporal logic) to check the model\n'
                          'In phase 4，find the counterexample to simulate the path with zingmodel designer.')

    # 帮助菜单 ——> 版本信息
    def action_about(self):
        QMessageBox.about(self.ui, '.:: Version ::.', 'Version：V2.1(2022.4.9)\nAuthor：Abb\nEmail：Mr_abb@163.com\n')

    # 反例联动
    def linkage(self):
        stm = self.ui.treeWidget_3.currentItem().text(0)
        loc = self.ui.treeWidget_3.currentItem().text(1)
        if stm == 'root' or loc[0] == 'R' or loc[0] == 'B':
            return
        if loc[0] == '/' or loc[0] == 'X':
            loc = loc[1:]
        self.model_designer.show_model_designer()
        if not self.model_designer.QMdiSubWins:  # QMdiSubWins为空
            self.model_designer.open_project(self.prj_path)
            self.model_designer.show_subWin(stm, loc)
            self.model_designer.ui.raise_()
        else:
            self.model_designer.show_subWin(stm, loc)
            self.model_designer.ui.raise_()

    # 反例显示
    def show_branch(self):
        self.ui.treeWidget_3.clear()
        ltl = self.ui.treeWidget_2.currentItem().text(0)
        if ltl not in self.branch.keys():
            return
        for i in range(0, len(self.branch[ltl])):
            if i == 0:
                root = QTreeWidgetItem(self.ui.treeWidget_3)
                tag = str(self.tree.get_node(self.branch[ltl][i]).tag)
                tag_list = tag.split('-')
                root.setText(0, tag)
                root.setText(1, '(-1,0)')
                root.setText(2, 'Depth-0')
                root.setText(3, str(self.tree.get_node(self.branch[ltl][i]).data))
            else:
                root = QTreeWidgetItem(self.ui.treeWidget_3)
                tag = str(self.tree.get_node(self.branch[ltl][i]).tag)
                tag_list = tag.split('-')
                root.setText(0, str(self.tree.get_node(self.branch[ltl][i]).data))
                root.setText(1, tag_list[0])
                root.setText(2, 'Depth-' + str(i))
                # root.setText(2, self.branch[ltl][i])
                root.setText(3, tag_list[1])
        # # 树状结构
        # if self.branch[ltl] is not None:
        #     root = QTreeWidgetItem(self.ui.treeWidget_3)
        #     root.setText(0, self.branch[ltl][0])
        #     print('branch', self.branch[ltl][0])
        #     tchild = root
        #     for i in range(1, len(self.branch[ltl])):
        #         child = QTreeWidgetItem(tchild)
        #         child.setText(0, self.branch[ltl][i])
        #         tchild.addChild(child)
        #         tchild = child
        # QTreeWidget().header().setSectionResizeMode(QHeaderView().ResizeToContents,3)
        self.ui.treeWidget_3.setAutoScroll(True)
        self.ui.treeWidget_3.expandToDepth(100)
        self.ui.treeWidget_3.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.treeWidget_3.header().setStretchLastSection(False)

    def tree_show_tips(self):
        QMessageBox.about(self.ui, '.:: Tip ::.', '.:: Tip ::.\n\n'
                                                  '-Loading and displaying the state space tree can clearly show each state space path.\n'
                                                  '-However, when the state space tree is too large, it may take a long time!')

    def load_state_space_tree(self):
        if self.ui.checkBox.isChecked():
            self.ui.treeWidget_2.header().setStretchLastSection(False)
            fmt = QTextCharFormat()
            fmt.setForeground(QBrush(QColor('green')))
            self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)
            self.ui.plainTextEdit.setPlainText(str(self.tree.subtree('--{\'root\':0}')))
            self.ui.label_9.show()
            self.ui.plainTextEdit.show()
        else:
            self.ui.treeWidget_2.header().setStretchLastSection(True)
            self.ui.label_9.hide()
            self.ui.plainTextEdit.hide()

    def get_usr_set_var_map(self):
        map = {}
        rowcount = self.ui.tableWidget.rowCount()
        for row in range(0, rowcount):
            value = self.ui.tableWidget.item(row, 3).text()
            if value == 'True':
                map[self.ui.tableWidget.item(row, 2).text()] = True
            elif value == 'False':
                map[self.ui.tableWidget.item(row, 2).text()] = False
            elif value.isdigit():
                map[self.ui.tableWidget.item(row, 2).text()] = int(value)
            else:
                map[self.ui.tableWidget.item(row, 2).text()] = value
        return map

    def show_result(self, txt):
        data = txt.split('-')
        # self.ui.treeWidget_2
        root = self.ui.treeWidget_2.topLevelItem(int(data[0]) + 1)
        if data[1] == 'error':
            root.setIcon(1, QIcon('../img/error.png'))
        else:
            root.setIcon(1, QIcon('../img/pass.png'))
        root.setText(1, data[2])

    def checking_thread(self):
        for row in range(0, self.ui.tableWidget_2.rowCount()):
            if str(self.ui.tableWidget_2.item(row, 2).checkState()) == 'PySide2.QtCore.Qt.CheckState.Checked':
                ltl = self.ui.tableWidget_2.item(row, 1).text()
                # try:
                # 检查计时
                start_time = time.time()
                branch = self.service.check_model(ltl, self.tree, self.dfs)  # do checking...
                end_time = time.time()
                # except Exception as e:
                #     QMessageBox.about(self.ui, '.:: Error ::.', e.__str__())
                #     return

                # 反例有无
                if branch is not None:
                    self.branch[ltl] = branch
                    txt = str(row) + '-' + 'error' + '-' + 'Find a counterexample，Time consumption: ' + str(round(end_time - start_time, 3)) + 's'
                else:
                    txt = str(row) + '-' + 'pass' + '-' + 'Pass，Time consumption: ' + str(round(end_time - start_time, 3)) + 's'
                self.checker_signal.send(txt)

    # 开始四阶段检查
    def start_phase4_checking(self):
        self.ui.treeWidget_2.clear()  # 清空数据
        self.ui.treeWidget_3.clear()
        self.branch = {}
        self.ui.treeWidget_2.setAutoScroll(True)
        self.ui.treeWidget_2.expandToDepth(100)
        self.ui.treeWidget_2.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.treeWidget_2.header().setStretchLastSection(False)

        self.ui.label_10.show()
        self.ui.label_10.setMovie(self.wait_gif)
        self.wait_gif.start()

        thread = threading.Thread(target=self.load_tree_thread)
        # 把子进程设置为守护线程，防止主线程退出子线程还在运行，必须在start()之前设置
        thread.setDaemon(True)
        thread.start()

    def load_tree_thread(self):
        # 内存消耗计算：状态空间树消耗
        gvm = self.get_usr_set_var_map()
        pid = os.getpid()
        p = psutil.Process(pid)

        start_time = time.time()
        mem_info_start = p.memory_full_info().uss / 1024

        self.tree = self.service.get_BMC_state_transition_tree(self.prj_path, gvm, self.ui.spinBox.value())
        mem_info_end = p.memory_full_info().uss / 1024
        end_time = time.time()
        use_time = str(round(end_time - start_time, 3))
        mem_use = mem_info_end - mem_info_start
        if self.mem_max < mem_use:
            self.mem_max = mem_use

        self.signal.send(use_time)

    def checker(self, use_time):
        self.wait_gif.stop()
        self.ui.label_10.hide()
        ssitem = QTreeWidgetItem(self.ui.treeWidget_2)
        ssitem.setText(0, "State Space Tree")
        QCoreApplication.processEvents()
        # 加载状态空间树到self.ui.plainTextEdit
        # 检查计时
        self.ui.plainTextEdit.setPlainText("Loading...")
        self.load_state_space_tree()  # 加载状态空间树

        for row in range(0, self.ui.tableWidget_2.rowCount()):
            if str(self.ui.tableWidget_2.item(row, 2).checkState()) == 'PySide2.QtCore.Qt.CheckState.Checked':
                root = QTreeWidgetItem(self.ui.treeWidget_2)
                ltl = self.ui.tableWidget_2.item(row, 1).text()
                root.setText(0, ltl)
                root.setText(1, 'Checking')

        # # 多线程检查
        self.thread = threading.Thread(target=self.checking_thread)
        # 把子进程设置为守护线程，防止主线程退出子线程还在运行，必须在start()之前设置
        self.thread.setDaemon(True)
        self.thread.start()

        caldata = self.service.calculation_compression_rate(self.tree, self.ui.spinBox.value())
        ssitem.setText(1, "Maximum memory consumption: " + str(self.mem_max) + "KB, " + "Time consumption: " + use_time + "s" + ", RBPS Nodes: " + caldata[
            0] + ";BMC Nodes: " + caldata[1] + ";Compression ratio: " + caldata[2])

    # def start_phase4_checking(self):
    #     self.ui.treeWidget_2.clear()  # 清空数据
    #     self.ui.treeWidget_3.clear()
    #     self.branch = {}
    #     self.ui.treeWidget_2.setAutoScroll(True)
    #     self.ui.treeWidget_2.expandToDepth(100)
    #     self.ui.treeWidget_2.header().setSectionResizeMode(QHeaderView.ResizeToContents)
    #     self.ui.treeWidget_2.header().setStretchLastSection(False)
    #
    #     gvm = self.get_usr_set_var_map()
    #     pid = os.getpid()
    #     p = psutil.Process(pid)
    #
    #     # 内存消耗计算
    #     mem_info_start = p.memory_full_info().uss / 1024
    #     if self.ui.radioButton_1.isChecked():
    #         self.tree = self.service.get_state_transition_tree(self.prj_path, gvm)
    #     else:
    #         self.tree = self.service.get_BMC_state_transition_tree(self.prj_path, gvm, self.ui.spinBox.value())
    #     mem_info_end = p.memory_full_info().uss / 1024
    #     summem = mem_info_end - mem_info_start
    #     item = QTreeWidgetItem(self.ui.treeWidget_2)
    #     item.setText(0, "状态空间树")
    #     item.setText(1, "生成状态空间树消耗内存" + str(mem_info_end - mem_info_start) + "KB")
    #     QCoreApplication.processEvents()
    #     # 加载状态空间树到self.ui.plainTextEdit
    #     # 检查计时
    #     self.load_state_space_tree()
    #     for row in range(0, self.ui.tableWidget_2.rowCount()):
    #         if str(self.ui.tableWidget_2.item(row, 2).checkState()) == 'PySide2.QtCore.Qt.CheckState.Checked':
    #             root = QTreeWidgetItem(self.ui.treeWidget_2)
    #             ltl = self.ui.tableWidget_2.item(row, 1).text()
    #             root.setText(0, ltl)
    #             root.setText(1, '检查中ing')
    #             try:
    #                 # 内存消耗计算
    #                 mem_info_start = p.memory_full_info().uss / 1024
    #                 txt = self.load_tree_and_checking(ltl, gvm, root)  # 检查LTL
    #                 mem_info_end = p.memory_full_info().uss / 1024
    #                 root.setText(1, txt)
    #                 summem += mem_info_end - mem_info_start
    #             except Exception as e:
    #                 QMessageBox.about(self.ui, '.:: Error ::.', e.__str__())
    #                 return
    #             # 实时刷新页面
    #             QApplication.processEvents()

    # 加载一阶段变量
    def set_phase1_data(self, prj_path):
        self.model_designer = ModelDesigner()  # 多次调用问题
        self.ui.treeWidget.clear()
        self.dfs = self.service.get_model_dfs(prj_path)
        self.var = self.service.get_model_var(prj_path)
        self.global_var_map = self.service.get_model_var_map(prj_path)
        self.prj_path = prj_path

        root = QTreeWidgetItem(self.ui.treeWidget)
        root.setIcon(0, QIcon('../img/pass.png'))
        root.setText(0, 'Pass！')
        root.setText(1, prj_path)
        self.ui.label_7.setText(prj_path)
        self.phase[0] = True
        self.set_phase2_data()

    # 加载二阶段变量
    def set_phase2_data(self):
        self.frame = 4
        # print(self.frame, 'frame4')
        stats.ui.frame_7.hide()
        stats.ui.frame_6.hide()
        stats.ui.frame_5.hide()
        stats.ui.frame_4.show()
        # 清空二阶段tableWidget
        for row in range(0, self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(0)
        # 清空三阶段tableWidget_2
        for row in range(2, self.ui.tableWidget_2.rowCount()):
            self.ui.tableWidget_2.removeRow(2)

        global_value_list = list(self.global_var_map.values())
        global_key_list = list(self.global_var_map.keys())
        for i in range(0, len(global_value_list)):
            rowcount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowcount)

            item0 = QTableWidgetItem(' [ Global ] ')
            item0.setTextColor(QColor('gray'))
            item0.setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

            self.ui.tableWidget.setItem(i, 0, item0)

            item1 = QTableWidgetItem(type(global_value_list[i]).__name__)
            item1.setTextColor(QColor('gray'))
            item1.setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

            item2 = QTableWidgetItem(global_key_list[i])
            item2.setTextColor(QColor('gray'))
            item2.setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

            item3 = QTableWidgetItem(str(global_value_list[i]))

            self.ui.tableWidget.setItem(i, 0, item0)
            self.ui.tableWidget.setItem(i, 1, item1)
            self.ui.tableWidget.setItem(i, 2, item2)
            self.ui.tableWidget.setItem(i, 3, item3)

            # if type(global_value_list[i]).__name__ == 'int':
            #     item4 = QTableWidgetItem(str(-sys.maxsize - 1))
            #     item5 = QTableWidgetItem(str(sys.maxsize))
            #     item4.setTextAlignment(Qt.AlignCenter)
            #     item5.setTextAlignment(Qt.AlignCenter)
            #     self.ui.tableWidget.setItem(i, 4, item4)
            #     self.ui.tableWidget.setItem(i, 5, item5)
            #
            # if type(global_value_list[i]).__name__ == 'bool':
            #     item4 = QTableWidgetItem('None')
            #     item4.setTextColor(QColor('gray'))
            #     item4.setFlags(
            #         Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            #     item5 = QTableWidgetItem('None')
            #     item5.setTextColor(QColor('gray'))
            #     item5.setFlags(
            #         Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            #     self.ui.tableWidget.setItem(i, 4, item4)
            #     self.ui.tableWidget.setItem(i, 5, item5)
            # 居中
            item0.setTextAlignment(Qt.AlignCenter)
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            item3.setTextAlignment(Qt.AlignCenter)
            # item4.setTextAlignment(Qt.AlignCenter)
            # item5.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.resizeColumnsToContents()
        # 设置三阶段界面
        self.set_phase3_data()

    # 加载三阶段界面
    def set_phase3_data(self):
        self.ui.tableWidget_2.setColumnWidth(1, 300)

    # 文件菜单 ——> 导入模型 / 导入模型按钮
    def open_file_button(self):
        self.phase = [False, False, False]
        try:
            dialog = QFileDialog()
            fileNames = dialog.getOpenFileName(None, 'model import', '.', '*.zprj')
            # self.dfs = self.service.get_model_dfs(fileNames[0])
            # self.var = self.service.get_model_var(fileNames[0])
            # zipc model
            # list_map = self.service.get_model(fileNames[0])

        except (IndexError, IOError):
            self.ui.treeWidget.clear()
            root = QTreeWidgetItem(self.ui.treeWidget)
            root.setIcon(0, QIcon('../img/error.png'))
            root.setText(0, 'fail！')
            root.setText(1, 'import model fail！')
        else:
            if (fileNames[0] != ''):
                self.set_phase1_data(fileNames[0])
                # print(self.dfs)
                # print(self.var)

    # 文件菜单 ——> 设计模型 / 设计模型按钮
    def design_button(self):
        self.model_designer.show_model_designer()

    # 文件菜单 ——> 结束
    def action_close(self):
        # 线程中退出
        os._exit(5)
        # sys.exit(app.exec_())

    # 第三阶段 ——> 添加按钮
    def add_button(self):
        self.add_ltl_ui.listWidget.clear()
        self.add_ltl_ui.show()
        self.add_ltl_ui.listWidget.addItems(self.global_var_map)
        self.add_ltl_ui.raise_()

    def list_double_clicked(self):
        self.add_ltl_ui.lineEdit.insert(self.add_ltl_ui.listWidget.currentItem().text())

    # 第三阶段 ——> 删除按钮
    def delete_button(self):
        index = self.ui.tableWidget_2.currentRow()
        if index != 0 and index != 1:
            self.ui.tableWidget_2.removeRow(index)

    # 第三阶段 ——> 添加LTL界面
    # pushButton_0
    def add_ltl_X(self):
        self.add_ltl_ui.lineEdit.insert('[X]{}')
        self.add_ltl_ui.lineEdit.cursorBackward(False, 1)

    # pushButton_1
    def add_ltl_G(self):
        self.add_ltl_ui.lineEdit.insert('[G]{}')
        self.add_ltl_ui.lineEdit.cursorBackward(False, 1)

    # pushButton_2
    def add_ltl_F(self):
        self.add_ltl_ui.lineEdit.insert('[F]{}')
        self.add_ltl_ui.lineEdit.cursorBackward(False, 1)

    # pushButton_3
    def add_ltl_W(self):
        QMessageBox.about(self.ui, '.:: Tip ::.',
                          '.::Please convert by the following rules::.\n'
                          '[W](LTL Weak-Until):        p[W]q ⇔ p[U]q[G]p\n')
        self.add_ltl_ui.raise_()

    # pushButton_4
    def add_ltl_U(self):
        self.add_ltl_ui.lineEdit.insert('{[U]}')
        self.add_ltl_ui.lineEdit.cursorBackward(False, 4)

    # pushButton_5
    def add_ltl_R(self):
        QMessageBox.about(self.ui, '.:: Tip ::.',
                          '.::Please convert by the following rules::.\n'
                          '[R](LTL Release):        p[R]q ⇔ p[U]q[G]p&q\n')
        self.add_ltl_ui.raise_()

    # pushButton_6
    def add_ltl_left_bracket(self):
        self.add_ltl_ui.lineEdit.insert('(')

    # pushButton_7
    def add_ltl_right_bracket(self):
        self.add_ltl_ui.lineEdit.insert(')')

    # pushButton_8
    def add_ltl_equal(self):
        self.add_ltl_ui.lineEdit.insert('==')

    # pushButton_9
    def add_ltl_not_equal(self):
        self.add_ltl_ui.lineEdit.insert('!=')

    # pushButton_10
    def add_ltl_greater(self):
        self.add_ltl_ui.lineEdit.insert('>')

    # pushButton_11
    def add_ltl_less(self):
        self.add_ltl_ui.lineEdit.insert('<')

    # pushButton_12
    def add_ltl_greater_and_equal(self):
        self.add_ltl_ui.lineEdit.insert('>=')

    # pushButton_13
    def add_ltl_less_and_equal(self):
        self.add_ltl_ui.lineEdit.insert('<=')

    # pushButton_14
    def add_ltl_and(self):
        self.add_ltl_ui.lineEdit.insert('&')

    # pushButton_15
    def add_ltl_or(self):
        self.add_ltl_ui.lineEdit.insert('|')

    # pushButton_16
    def add_ltl_imply(self):
        # self.add_ltl_ui.lineEdit.insert('⇒')
        QMessageBox.about(self.ui, '.:: LTL input instructions ::.',
                          '.::Instructions::.\n'
                          'Please use {} when using LTL operator to confirm the scope of the operator so that the software can check it:\n'
                          '[G]{p}、[F]{p}、[X]{p}、{p[U]q}\n'
                          'Sample：\n'
                          '[G]{ a>=0 & [F]{b==True} | {c<1[U]d>0} | [X]{e} }\n\n'
                          '.::Operator support range::.\n'
                          'At present, the software only supports basic logical expressions, and the unrealized LTL operators can be converted by the existing basic operators.\n\n'
                          '.::Already implemented operators::.\n'
                          'LTL: [G] [F] [X] [U] \n'
                          'Logical operator:     == != > < >= <= & |\n\n'
                          '.::Operator not implemented::.\n'
                          '⇒（Logical implication）:            p⇒q ⇔ ¬p|q\n'
                          '[W]（LTL Weak-Until）:      p[W]q ⇔ p[U]q[G]p\n'
                          '[R]（LTL Release）:         p[R]q ⇔ p[W]p&q\n\n'
                          '.::Conversion Sample::.\n'
                          'p==0⇒q>3 ≡ p!=0|q>3\n')
        self.add_ltl_ui.raise_()

    # pushButton_17
    def add_ltl_cancel(self):
        self.add_ltl_ui.lineEdit.setText(None)
        self.add_ltl_ui.close()

    # pushButton_18
    def add_ltl_confirm(self):
        text = self.add_ltl_ui.lineEdit.text()
        rowcount = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(rowcount)

        self.ui.tableWidget_2.setItem(rowcount, 0, QTableWidgetItem('LTL Check'))
        self.ui.tableWidget_2.setItem(rowcount, 1, QTableWidgetItem(text))
        # self.ui.tableWidget_2.setItem(rowcount, 2, QTableWidgetItem('检查'))
        item = QTableWidgetItem('Check')
        item.setCheckState(Qt.CheckState.Checked)
        self.ui.tableWidget_2.setItem(rowcount, 2, item)

        self.add_ltl_ui.lineEdit.setText(None)
        self.add_ltl_ui.close()

    # 上一步按钮
    def previous_button(self):
        if (self.frame == 7):
            stats.ui.frame_7.hide()
            stats.ui.frame_6.show()
            self.ui.progressBar.setValue(75)
            self.frame -= 1
        elif (self.frame == 6):
            stats.ui.frame_6.hide()
            stats.ui.frame_5.show()
            self.ui.progressBar.setValue(50)
            self.frame -= 1
        elif (self.frame == 5):
            stats.ui.frame_5.hide()
            stats.ui.frame_4.show()
            self.ui.progressBar.setValue(25)
            self.frame -= 1
        else:
            pass

    # 下一步按钮
    def next_button(self):
        global_value_list = list(self.global_var_map.values())
        if (self.frame == 4):
            if self.phase[0] == True:
                stats.ui.frame_4.hide()
                stats.ui.frame_5.show()
                self.ui.progressBar.setValue(50)
                self.frame += 1
            else:
                QMessageBox.about(self.ui, '.:: Tip ::.', 'Please import the model correctly!')
        elif (self.frame == 5):
            for i in range(0, len(global_value_list)):
                if self.ui.tableWidget.item(i, 1).text() == 'int':
                    value = int(self.ui.tableWidget.item(i, 3).text())
                    self.phase[1] = self.service.check_int(value)
                elif self.ui.tableWidget.item(i, 1).text() == 'bool':
                    value = self.ui.tableWidget.item(i, 3).text()
                    self.phase[1] = self.service.check_bool(value)
                if self.phase[1] == False:
                    self.ui.tableWidget.selectRow(i)
                    break
            if self.phase[1] == True:
                stats.ui.frame_5.hide()
                stats.ui.frame_6.show()
                self.ui.progressBar.setValue(75)
                self.frame += 1
            else:
                QMessageBox.about(self.ui, '.:: Tip ::.', 'Please set the variable correctly!')
        elif (self.frame == 6):
            self.phase[2] = True
            for i in range(0, self.ui.tableWidget_2.rowCount()):
                ltl = self.ui.tableWidget_2.item(i, 1).text()
                # 检查LTL语句
                if ltl == 'Threshold' or ltl == 'Unreachable':
                    continue
                self.phase[2] = self.service.check_ltl(ltl, self.global_var_map)
                if self.phase[2] == False:
                    self.ui.tableWidget_2.selectRow(i)
                    break

            if self.phase[2] == True:
                stats.ui.frame_6.hide()
                stats.ui.frame_7.show()
                self.ui.progressBar.setValue(100)
                self.frame += 1
                self.start_phase4_checking()
            else:
                # do cheeck
                QMessageBox.about(self.ui, '.:: Tip ::.', 'Error in input validation attribute!')
        else:
            pass


if __name__ == '__main__':
    app = QApplication([])
    stats = MainWindow()

    # 窗口居中
    stats.ui.setGeometry(0, 0, 800, 800)
    qRect = stats.ui.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qRect.moveCenter(centerPoint)
    stats.ui.move(qRect.topLeft())

    stats.ui.frame_7.hide()
    stats.ui.frame_6.hide()
    stats.ui.frame_5.hide()
    stats.ui.frame_4.show()

    stats.ui.show()
    app.exec_()
