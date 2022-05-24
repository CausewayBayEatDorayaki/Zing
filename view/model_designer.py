import sys

import pandas
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QKeySequence
from PySide2.QtUiTools import QUiLoader

from service.model_designer_service import ModelDesignerService
from view.table import Table

from PySide2.QtCore import QFileInfo, Qt
from PySide2.QtWidgets import *
from PySide2 import QtGui
import os


class ModelDesigner:
    def __init__(self):
        self.QMdiSubWins = {}
        self.project_path = None  # workspace
        self.tree = QTreeWidget()
        self.varWin = None

        self.model_designer_service = ModelDesignerService()
        self.ui = QUiLoader().load('../ui/model_designer.ui')
        self.ui.setWindowIcon(QIcon('../img/zing.png'))
        self.new_project_ui = QUiLoader().load('../ui/new_project.ui')
        self.new_project_ui.setWindowIcon(QIcon('../img/zing.png'))
        self.set_stm_ui = QUiLoader().load('../ui/stm_set.ui')
        self.set_stm_ui.setWindowIcon(QIcon('../img/zing.png'))
        self.ui.dockWidget.close()

        # 加入Ctrl+S保存快捷键
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self.ui)
        self.shortcut.activated.connect(self.action_save)
        # 加入Ctrl+O卡开快捷键
        self.shortcut = QShortcut(QKeySequence("Ctrl+O"), self.ui)
        self.shortcut.activated.connect(self.action_open)
        # 加入Ctrl+P打开案例
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self.ui)
        self.shortcut.activated.connect(self.action_powerlink)
        # 加入Ctrl+T打开案例
        self.shortcut = QShortcut(QKeySequence("Ctrl+T"), self.ui)
        self.shortcut.activated.connect(self.actionTcp_ip)

        # 文件菜单
        self.ui.actionnewproject.triggered.connect(self.action_new_project)
        self.ui.actionnewstm.triggered.connect(self.action_new_stm)
        self.ui.actionopen.triggered.connect(self.action_open)
        self.ui.actionsave.triggered.connect(self.action_save)
        # 视图菜单
        self.ui.actionfilemanager.triggered.connect(self.action_file_manager)
        # 帮助菜单
        self.ui.actionabout.triggered.connect(self.action_about)
        self.ui.actionhelp.triggered.connect(self.action_help)
        # 模型案例菜单
        self.ui.actionPowerlink.triggered.connect(self.action_powerlink)
        self.ui.actionModbus.triggered.connect(self.action_modbus)

        # STM设置UI
        self.set_stm_ui.pushButton_confirm.clicked.connect(self.confirm_set_stm_button)
        # 新建工程UI
        self.new_project_ui.toolButton.clicked.connect(self.open_folder_get_path_toolButton)
        self.new_project_ui.pushButton.clicked.connect(self.create_new_project_button)

        # 右键菜单
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.generate_menu)

    # ************************************************************************************
    # ********************************* ModelDesigner UI *********************************
    # ************************************************************************************


    def show_subWin(self, item, loc):
        loc = loc[1:len(loc) - 1]
        eas = loc.split(',')
        row = 0
        df_data = self.model_designer_service.load_stm_file(self.project_path + '/' + item)
        for i in range(0, len(df_data[0])):
            if eas[0] == df_data[0][i]:
                row = i
        if item in self.QMdiSubWins.keys():
            self.QMdiSubWins[item].show()
            self.QMdiSubWins[item].raise_()
            self.QMdiSubWins[item].Table.tableWidget.clearSelection()
            self.QMdiSubWins[item].Table.tableWidget.item(row + 2, int(eas[1]) + 2).setSelected(True)

            self.QMdiSubWins[item].setWindowTitle(item)
            self.QMdiSubWins[item].tableChanged = False

        else:
            df_data = self.model_designer_service.load_stm_file(self.project_path + '/' + item)
            self.new_stm_window(item, len(df_data[1]), len(df_data[0]))
            self.QMdiSubWins[item].Table.set_table(df_data[0], df_data[1], df_data[2])
            self.QMdiSubWins[item].setWindowTitle(item)

            self.QMdiSubWins[item].raise_()
            self.QMdiSubWins[item].Table.tableWidget.clearSelection()
            self.QMdiSubWins[item].Table.tableWidget.item(row + 2, int(eas[1]) + 2).setSelected(True)

            self.QMdiSubWins[item].setWindowTitle(item)
            self.QMdiSubWins[item].tableChanged = False

    # 删除STM文件
    def delete_file(self, filename):
        self.model_designer_service.delete_file(self.project_path, filename)
        print(self.project_path, filename)

    # 右键菜单绑定函数
    def generate_menu(self, pos):
        item = self.tree.currentItem().text(0)
        print(item)
        if item:
            menu = QMenu()
            item1 = menu.addAction(u"New STM")
            item2 = menu.addAction(u"Delete")
            item3 = menu.addAction(u"Save")
            action = menu.exec_(self.tree.mapToGlobal(pos))
            if action == item1:
                self.action_new_stm()
            elif action == item2:
                splitems = item.split('.')
                if len(splitems) == 2:
                    if splitems[1] == 'stm':
                        if item in self.QMdiSubWins.keys():
                            self.QMdiSubWins[item].close()
                            del self.QMdiSubWins[item]
                        self.delete_file(item)
                        self.tree.clear()
                        self.set_dockwidget(self.project_path)
                    elif splitems[1] == 'var':
                        QMessageBox.about(self.ui, '.:: Tip ::.', '\nThe built-in file of the project cannot be deleted!')
                    elif splitems[1] == 'zprj':
                        QMessageBox.about(self.ui, '.:: Tip ::.', '\nThe project startup file cannot be deleted!')
                    else:
                        self.delete_file(item)
                else:
                    QMessageBox.about(self.ui, '.:: Tip ::.', '\nProtected files cannot be deleted!')

            elif action == item3:
                self.action_save()
            else:
                return

    # 显示ModelDesigner
    def show_model_designer(self):
        self.ui.show()

    # 文件菜单 ——> 新建工程
    def action_new_project(self):
        self.new_project_ui.show()
        self.new_project_ui.raise_()

    # 文件菜单 ——> 新建STM
    def action_new_stm(self):
        self.set_stm_ui.show()

    # 打开案例
    def open_project(self, prj_path):
        # fileNames = ['../model_example/zingprj/tcpip_handshake.zprj']
        # 内部数据置空
        key_list = list(self.QMdiSubWins.keys())
        for key in key_list:
            self.QMdiSubWins[key].setAttribute(Qt.WA_DeleteOnClose, True)  # 析构
        self.QMdiSubWins.clear()
        self.ui.mdiArea.closeAllSubWindows()
        self.tree.clear()
        self.varWin = None

        path = self.model_designer_service.designer_get_model_path(prj_path)
        self.set_dockwidget(path)
        self.ui.dockWidget.show()
        self.new_project_ui.close()
        self.project_path = path

    # 文件菜单 ——> 打开工程
    def action_open(self):
        fileNames = QFileDialog.getOpenFileName(None, 'Open Zing Project', '.', '*.zprj')
        if fileNames[0] != '':
            self.open_project(fileNames[0])

    # 文件菜单 ——> 保存项目
    def action_save(self):
        if self.project_path is not None:
            # 保存stm
            if self.QMdiSubWins != {}:
                stm_name_list = list(self.QMdiSubWins.keys())
                dfs = {}
                for name in stm_name_list:
                    self.QMdiSubWins[name].Table.fresh()
                    self.QMdiSubWins[name].setWindowTitle(name)
                    self.QMdiSubWins[name].tableChanged = False
                    dfs[name] = self.QMdiSubWins[name].Table.get_dataFrame()
                self.model_designer_service.save_stm_files(self.project_path, stm_name_list, dfs)
                self.tree.expandAll()
            # 保存var
            if self.varWin is not None:
                text = self.varWin.textEdit.toPlainText()
                self.model_designer_service.save_var_file(self.project_path, self.varWin.table_name, text)
                self.varWin.tableChanged = False
                self.varWin.setWindowTitle(self.varWin.table_name)
                self.tree.expandAll()

    # 视图菜单 ——> 资源管理器显示
    def action_file_manager(self):
        self.ui.dockWidget.show()

    # 帮助菜单 ——> 使用说明
    def action_help(self):
        QMessageBox.about(self.ui, '.:: Instructions ::.',
                          '~~~State Transition Script Matrix (STSM) Modeling Tool~~~\n\n'

                          '1. Events and status\n'
                          '      1)The first column of the table is the events.\n'
                          '      2)The first row of the table is the states.\n\n'

                          '2. Cell contents\n'
                          '      1)the cell needs to use Python script to describe the model structure. Please fill it in strict accordance with the python script specification.\n'
                          '      2)JUMP(n) is the only built-in function, and the parameter indicates the state subscript to jump.\n\n'

                          '3. Variable definition\n'
                          '      1)All variables that appear in the STSM model need to be defined in the .var file.\n'
                          '      2)The state variable needs to be defined as an integer type in the form of \'STMNAME_STATE\', which represents the subscript corresponding to the initial state in the table (the column subscript in the table).\n'
                          '      1)When defining a variable, you need to assign an initial value to the variable.\n\n'

                          '4. Variable naming restrictions\n'
                          '      1)Substrings are not allowed，such as x_Play is defined ,and x_Play_1 is not allowed to be defined,but x_Play_0 or x_Play_1 is allowed.\n\n'
                          )

    # 帮助菜单 ——> 版本信息
    def action_about(self):
        QMessageBox.about(self.ui, '.:: Version ::.', 'Version：V2.1(2022.4.9)\nAuthor：Abb\nEmail：Mr_abb@163.com\n')

    # 模型案例菜单 ——> powerlink
    def action_powerlink(self):
        prj_path = '../model_example/Powerlink/Powerlink.zprj'
        self.open_project(prj_path)

    # 模型案例菜单 ——> modbus
    def action_modbus(self):
        prj_path = '../model_example/Modbus/Modbus.zprj'
        self.open_project(prj_path)

    # 模型案例菜单 ——> tcp/ip
    def actionTcp_ip(self):
        prj_path = '../model_example/tcpip_handshake/tcpip_handshake.zprj'
        self.open_project(prj_path)

    # 实例化Table窗口
    def new_stm_window(self, table_name, col_number, row_number):
        # 实例化多文档界面对象
        sub = myQMdiSubWindow()
        sub.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # 成员变量赋值保存应用状态信息
        self.QMdiSubWins[table_name] = sub
        sub.Table = Table(table_name, col_number, row_number)
        sub.table_name = table_name
        sub.project_path = self.project_path

        # 向sub内添加内部控件
        sub.Table.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        sub.Table.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 设置table的水平滚动条
        sub.Table.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        sub.setWidget(sub.Table.tableWidget)
        # 设置新建子窗口的标题
        sub.setWindowTitle(table_name)
        # 将子窗口添加到Mdi区域

        self.ui.mdiArea.addSubWindow(sub)
        sub.setMinimumSize(600, 500)  # 根据输入的调节大小

        # 子窗口显示
        sub.show()
        sub.setTableMonitor()

    # 实例化变量输入窗口
    def new_var_window(self, table_name):
        # 实例化多文档界面对象
        sub = myQMdiSubWindow()
        sub.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # 成员变量赋值保存应用状态信息
        self.varWin = sub
        sub.table_name = table_name
        sub.project_path = self.project_path

        # 向sub内添加内部控件
        sub.setWidget(sub.textEdit)
        # 设置新建子窗口的标题
        sub.setWindowTitle(table_name)
        # 将子窗口添加到Mdi区域

        self.ui.mdiArea.addSubWindow(sub)
        sub.setMinimumSize(600, 500)  # 根据输入的调节大小
        # 子窗口显示
        sub.show()
        # sub.setTableMonitor()

    # 设置文件树加入dockWidget
    def set_dockwidget(self, path):
        self.tree.setColumnCount(1)
        self.tree.setColumnWidth(0, 50)
        self.tree.setHeaderLabels(["Project"])
        # self.tree.setIconSize(Qt.QSize(25, 25))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.doubleClicked.connect(self.double_clicked_tree)

        dirs = os.listdir(path)
        fileInfo = QFileInfo(path)
        fileIcon = QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        root = QTreeWidgetItem(self.tree)
        root.setText(0, path.split('/')[-1])
        root.setIcon(0, QtGui.QIcon(icon))
        self.create_tree(dirs, root, path)
        self.ui.dockWidget.setWidget(self.tree)
        self.tree.expandAll()
        # self.setCentralWidget(self.tree)
        # QApplication.processEvents()

    # 创建资源树
    def create_tree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '\\' + i
            if os.path.isdir(path_new):
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))
                dirs_new = os.listdir(path_new)
                self.create_tree(dirs_new, child, path_new)
            else:
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))

    # 双击treeWidget事件
    def double_clicked_tree(self):
        item = self.tree.currentItem().text(0)
        splitems = item.split('.')
        if len(splitems) == 2:
            if splitems[1] == 'stm':
                if item in self.QMdiSubWins:
                    self.QMdiSubWins[item].show()
                    self.QMdiSubWins[item].setFocus()
                else:
                    df_data = self.model_designer_service.load_stm_file(self.project_path + '/' + item)
                    self.new_stm_window(item, len(df_data[1]), len(df_data[0]))
                    self.QMdiSubWins[item].Table.set_table(df_data[0], df_data[1], df_data[2])
                    self.QMdiSubWins[item].setWindowTitle(item)
                    self.QMdiSubWins[item].tableChanged = False
            elif splitems[1] == 'var':
                if self.varWin is not None:
                    self.varWin.show()
                    self.varWin.setFocus()
                else:
                    text = self.model_designer_service.load_var_file(self.project_path, item)
                    self.new_var_window(item)
                    self.varWin.textEdit.setText(text)
                    self.varWin.tableChanged = False
                    self.varWin.setWindowTitle(item)

    # ************************************************************************************
    # ************************************ STM设置 UI *************************************
    # ************************************************************************************

    # 添加STM确认按钮
    def confirm_set_stm_button(self):
        if self.project_path is None and self.project_path == None:
            self.set_stm_ui.close()
            QMessageBox.about(self.ui, '.:: Tip ::.', '\nPlease open or create a new project first!')
        else:
            stm_name = self.set_stm_ui.lineEdit.text() + '.stm'
            if (os.path.exists(self.project_path + '/' + stm_name)):
                QMessageBox.about(self.ui, '.:: Tip ::.', '\nSTM project already exists!')
                self.set_stm_ui.raise_()
            else:
                col_number = self.set_stm_ui.spinBox_column.value()
                row_number = self.set_stm_ui.spinBox_row.value()
                self.new_stm_window(stm_name, col_number, row_number)
                # self.set_stm_ui.lineEdit.setText(stm_name)

                col_str = []
                row_str = []
                for i in range(0, col_number):   col_str.append('')
                for i in range(0, col_number):   row_str.append('')
                df = pandas.DataFrame(columns=col_str, index=row_str)
                self.model_designer_service.create_stm_file(self.project_path, stm_name, df)
                self.tree.clear()

                self.set_dockwidget(self.project_path)
                self.set_stm_ui.close()

    # ************************************************************************************
    # ************************************ 新建工程 UI *************************************
    # ************************************************************************************

    # 创建按钮菜单
    def create_new_project_button(self):
        workspace_path = self.new_project_ui.lineEdit_path.text()
        prj_name = self.new_project_ui.lineEdit_name.text()
        prj_path = workspace_path + '/' + prj_name
        if (workspace_path == '' or prj_name == ''):
            QMessageBox.about(self.ui, '.:: Tip ::.', '\nProject path or project name cannot be empty!')
            self.new_project_ui.raise_()
            return
        # 判断路径是否存在
        isExists = os.path.exists(prj_path)
        # 判断结果
        if not isExists:
            # 内部数据置空
            key_list = list(self.QMdiSubWins.keys())
            for key in key_list:
                self.QMdiSubWins[key].setAttribute(Qt.WA_DeleteOnClose, True)
            self.QMdiSubWins.clear()
            self.ui.mdiArea.closeAllSubWindows()
            self.tree.clear()
            self.varWin = None

            # 调用service创建工程函数
            self.model_designer_service.create_project(prj_path, prj_name)
            self.project_path = prj_path
            self.set_dockwidget(prj_path)
            self.ui.dockWidget.show()
            self.new_project_ui.close()
            self.new_project_ui.lineEdit_name.setText(self.new_project_ui.lineEdit_name.text() + '_plus')
        else:
            # 如果工程存在则不创建，并提示
            QMessageBox.about(self.ui, '.:: Tip ::.', prj_path + '\nProject already exists! Please modify the project name!')
            self.new_project_ui.raise_()

    # 浏览资源管理器按钮（设置工作空间）
    def open_folder_get_path_toolButton(self):
        path = QFileDialog.getExistingDirectory(self.ui, "Select workspace folder", "./")
        self.new_project_ui.lineEdit_path.setText(path)
        self.new_project_ui.lineEdit_name.setText('ProjectName')
        self.new_project_ui.raise_()


class myQMdiSubWindow(QMdiSubWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('../img/zing.png'))
        self.Table = None
        self.textEdit = QTextEdit()
        self.table_name = ''
        self.project_path = ''
        self.tableChanged = False
        self.isclosed = False
        self.textEdit.textChanged.connect(self.fresh)

    def setTableMonitor(self):
        self.Table.tableWidget.cellChanged.connect(self.fresh)
        #self.Table.tableWidget.documentChanged.connect(self.fresh)

    def fresh(self):
        self.tableChanged = True
        self.setWindowTitle(self.table_name + '*')

    def showDialog(self):
        self.isclosewindow = True
        vbox = QVBoxLayout()  # 纵向布局
        hbox = QHBoxLayout()  # 横向布局
        panel = QLabel()
        panel.setText("文件尚未保存确定关闭？")
        self.dialog = QDialog()
        self.dialog.resize(100, 100)
        self.okBtn = QPushButton("Confirm")
        self.cancelBtn = QPushButton("Cancel")

        # 绑定事件
        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        self.dialog.setWindowTitle('.:: Tip ::.')
        # okBtn.move(50,50)#使用layout布局设置，因此move效果失效
        # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

        # 消息label与按钮组合纵向布局
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        self.dialog.setWindowModality(Qt.ApplicationModal)  # 该模式下，只有该dialog关闭，才可以关闭父界面
        self.dialog.exec_()

    # 槽函数如下：
    def ok(self):
        self.dialog.close()

    def cancel(self):
        self.dialog.close()
        self.isclosewindow = False

    def closeEvent(self, closeEvent):
        if (self.tableChanged == True):
            self.showDialog()
            if (self.isclosewindow == False):
                closeEvent.ignore()
            else:
                self.isclosed = True


if __name__ == '__main__':
    app = QApplication([])
    stats = ModelDesigner()

    # 窗口居中
    qRect = stats.ui.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qRect.moveCenter(centerPoint)
    stats.ui.move(qRect.topLeft())

    stats.ui.show()
    app.exec_()
