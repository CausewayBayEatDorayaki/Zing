import pandas
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QTableWidget, QTextEdit, QTableWidgetItem, QMenu, QHeaderView, QAbstractItemView


class Table:
    def __init__(self, stm_name, col, row):
        self.rowNumber = row
        self.colNumber = col
        self.header_visible = False
        self.tableWidget = QTableWidget(self.rowNumber + 2, self.colNumber + 2)
        self.load_tableWidget()
        self.df = pandas.DataFrame()
        self.tableWidget.horizontalHeader().setSelectionMode(QAbstractItemView.NoSelection)
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.set_visible()

    def set_visible(self):
        self.tableWidget.horizontalHeader().setVisible(self.header_visible)
        self.tableWidget.verticalHeader().setVisible(self.header_visible)

    def set_table(self, row, col, df):
        for i in range(0, len(col)):
            # 设置表头
            textstr = str(col[i])
            itemNew = QTableWidgetItem(textstr) # 在单元格中新插入一个item 并设定格式以及设定值
            itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
            self.tableWidget.setItem(0, i + 2, itemNew)
            # 设置单元格
            col_list = df[col[i]].values
            for j in range(0, len(row)):
                textstr = str(col_list[j])
                itemNew = QTableWidgetItem(textstr)  # 在单元格中新插入一个item 并设定格式以及设定值
                self.tableWidget.setItem(j + 2, i + 2, itemNew)
                if textstr is '/' or textstr is 'X':
                    itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
        for i in range(0, len(row)):
            # 设置行头
            textstr=str(row[i])
            itemNew = QTableWidgetItem(textstr)  # 在单元格中新插入一个item 并设定格式以及设定值
            itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
            self.tableWidget.setItem(i + 2, 0, itemNew)
        self.tableWidget.resizeColumnsToContents()
        self.fresh()

    def get_dataFrame(self):
        df = self.df
        return df

    def load_tableWidget(self):
        rowNumber = self.rowNumber
        colNumber = self.colNumber

        #setHeaderText(HStr=, VStr=['', '', '', '', ])

        for i in range(0, rowNumber + 2):
            for j in range(0, colNumber + 2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(''))

        self.tableWidget.doubleClicked.connect(self.edit)
        self.tableWidget.itemSelectionChanged.connect(self.fresh)

        # 初始化表的格式、样式
        self.initTable()
        # self.setHeaderText(HStr=['poweroff', 'pause', 'play'], VStr=['poweroff', 'play', 'off', 'pause', ])
        # 实例化一个textEdit
        self.textEdit = QTextEdit()
        self.textEdit.setAlignment(QtCore.Qt.AlignTop)
        self.textEdit.setHidden(True)
        self.textEdit.blockSignals(True)
        # 表格操作时用到的相关变量 先声明
        self.previousRow = 0  # 用于保存上次编辑结束的行号
        self.previousCol = 0  # 用于保存上次编辑结束的列号
        self.changedFlag = False  # 标志赋值 防止误操作
        # 右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

    # 用于设定表格的前两行、两列的宽度大小，设置列号、行号 以及背景颜色设定为灰色
    def initTable(self):
        self.tableWidget.setRowHeight(0, 40)
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget.verticalHeader().setMinimumSectionSize(1)
        self.tableWidget.setRowHeight(1, 20)
        self.tableWidget.setColumnWidth(1, 20)

        rowNumber = self.rowNumber
        colNumber = self.colNumber

        for i in range(2, rowNumber + 2):
            self.tableWidget.setRowHeight(i, 80)
        for i in range(2, colNumber + 2):
            self.tableWidget.setColumnWidth(i, 160)

        rowStr = ['S', ''] + [i for i in range(rowNumber)]
        for i in range(0, rowNumber + 2):
            # 设置为灰色  且填充好对应的文字
            item = QTableWidgetItem(str(rowStr[i]))
            item.setTextAlignment(Qt.AlignCenter)
            # 设置字体的大小和颜色
            item.setBackgroundColor(QColor('gray'))
            self.tableWidget.setItem(i, 1, item)

        colStr = ['E', ''] + [i for i in range(colNumber)]
        for i in range(0, colNumber + 2):
            # 设置为灰色  且填充好对应的文字
            item = QTableWidgetItem(str(colStr[i]))
            item.setTextAlignment(Qt.AlignCenter)
            # 设置字体的大小和颜色
            item.setBackgroundColor(QColor('gray'))
            self.tableWidget.setItem(1, i, item)

    # 用于设定表格的行列标题，设置字体为蓝色、红色
    def setHeaderText(self, HStr, VStr):
        ##
        rowNumber = self.rowNumber
        colNumber = self.colNumber

        # print(len(VStr))
        # print(rowNumber)

        ## 如果当前传入的列标题与实际列数不吻合，则默认添加' '
        if len(VStr) < rowNumber:
            vStrPlus = ['' for i in range(rowNumber - len(VStr))]
            #print(vStrPlus)
            VStr = VStr + vStrPlus
        for i in range(0, rowNumber):
            # 设置为蓝色  且填充好对应的文字
            item = QTableWidgetItem(str(VStr[i]))
            item.setTextAlignment(Qt.AlignCenter)
            item.setTextColor(QColor('blue'))
            self.tableWidget.setItem(i + 2, 0, item)

        ## 如果当前传入的列标题与实际列数不吻合，则默认添加' '
        if len(HStr) < colNumber:
            hStrPlus = ['' for i in range(colNumber - len(HStr))]
            HStr = HStr + hStrPlus
        for i in range(0, colNumber):
            # 设置为红色  且填充好对应的文字
            item = QTableWidgetItem(str(HStr[i]))
            item.setTextAlignment(Qt.AlignCenter)
            item.setTextColor(QColor('red'))
            self.tableWidget.setItem(0, i + 2, item)

    # 右键菜单绑定函数
    def generateMenu(self, pos):
        item = self.tableWidget.currentItem()
        if item:
            row = item.row()
            col = item.column()
            #print(row, col)
            if row > 1 and col > 1:
                menu = QMenu()
                item1 = menu.addAction(u"Normal cell")
                item2 = menu.addAction(u"Ignore cell")
                item3 = menu.addAction(u"Unreachable cell")
                menu.addSeparator()
                item4 = menu.addAction(u"Add a row")
                item5 = menu.addAction(u"Add a column")
                item6 = menu.addAction(u"Delete entire row")
                item7 = menu.addAction(u"Delete entire column")
                menu.addSeparator()
                item8 = menu.addAction(u"Cell compact")
                item9 = menu.addAction(u"Cell default width and height")
                item10 = menu.addAction(u"Cell width adaptation")
                item11 = menu.addAction(u"Cell height adaptation")
                item12 = menu.addAction(u"Cell width and height adaptation")
                item13 = menu.addAction(u"Free adjustment cell")

                action = menu.exec_(self.tableWidget.mapToGlobal(pos))
                if action == item1:
                    self.tableWidget.item(row, col).setText('')
                    self.tableWidget.item(row, col).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                elif action == item2:
                    self.tableWidget.item(row, col).setText('/')
                    self.tableWidget.item(row, col).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                elif action == item3:
                    self.tableWidget.item(row, col).setText('X')
                    self.tableWidget.item(row, col).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                elif action == item4:
                    #print('您选了增加一行', self.tableWidget.item(row, col).text())
                    self.newRow(row, col)
                elif action == item5:
                    #print('您选了增加一列', self.tableWidget.item(row, col).text())
                    self.newCol(row, col)
                elif action == item6:
                    #print('您选了删除整行', self.tableWidget.item(row, col).text())
                    self.delRow(row, col)
                elif action == item7:
                    #print('您选了删除整列', self.tableWidget.item(row, col).text())
                    self.delCol(row, col)
                elif action == item8:
                    for i in range(2, self.rowNumber + 2):
                        self.tableWidget.setRowHeight(i, 80)
                    for i in range(2, self.colNumber + 2):
                        self.tableWidget.setColumnWidth(i, 130)
                        self.tableWidget.setColumnWidth(0, 130)
                elif action == item9:
                    for i in range(2, self.rowNumber + 2):
                        self.tableWidget.setRowHeight(i, 80)
                    for i in range(2, self.colNumber + 2):
                        self.tableWidget.setColumnWidth(i, 160)
                elif action == item10:
                    for i in range(2, self.rowNumber + 2):
                        self.tableWidget.setRowHeight(i, 80)
                    self.tableWidget.resizeColumnsToContents()
                elif action == item11:
                    for i in range(2, self.colNumber + 2):
                        self.tableWidget.setRowHeight(i, 160)
                    self.tableWidget.resizeRowsToContents()
                elif action == item12:
                    self.tableWidget.resizeColumnsToContents()
                    self.tableWidget.resizeRowsToContents()
                elif action == item13:
                    self.header_visible = not self.header_visible
                    self.set_visible()
                else:
                    return

    # 双击单元格后进行的操作
    def edit(self):
        item = self.tableWidget.currentItem()
        # 如果当前单元格有 item
        if item:
            row = item.row()
            col = item.column()
            if row < 2 or col < 2:
                self.previousRow = 0
                self.previousCol = 0
                return
            print('edit:', row, col)
            self.previousRow = row
            self.previousCol = col

            # 建立一个textEdit
            textEdit = QTextEdit()  # Create
            # 初始化textEdit 的值
            textEdit.setText(self.tableWidget.item(row, col).text())
            self.tableWidget.setCellWidget(row, col, textEdit)  # 插入单元格对应的位置中
            self.textEdit = textEdit  # 保存该textEdit变量 否则会消失 用于退出时更新值给表格
            self.changedFlag = True  # 标志赋值 防止误操作

    # 当前所选择单元格变化时  所触发的函数
    def fresh(self):
        item = self.tableWidget.currentItem()
        if item:
            row = item.row()
            col = item.column()
            #print('fresh', row, col)
        # 仅赋值结束后进行的操作
        if item and self.changedFlag:
            data = self.textEdit.toPlainText()  # 获取值
            self.tableWidget.removeCellWidget(self.previousRow, self.previousCol)  # 删除单元格中的textEdit控件
            itemNew = QTableWidgetItem(data)  # 在单元格中新插入一个item 并设定格式以及设定值
            if data is '/' or data is 'X':
                itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
            else:
                itemNew.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(self.previousRow, self.previousCol, itemNew)
            self.changedFlag = False
            # 将所有有效内容存储为一个list  再转化成DataFrame
        self.saveFile()

    # 将所有有效内容存储为一个list  再转化成DataFrame
    def saveFile(self):
        #  可以选择保存位置
        # savePath = QtGui.QFileDialog.getSaveFileName(None, "Blood Hound",
        #                                              "Testing.csv", "CSV files (*.csv)")
        #  新建列表用于将表格中的所有值保存
        df_list = []
        for row in range(self.tableWidget.rowCount()):
            df_list2 = []
            for col in range(self.tableWidget.columnCount()):
                table_item = self.tableWidget.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        #  去除表头以及行列号
        data = [_[2:] for _ in df_list[2:]]
        #print('saveFile', data)

        #  将数值进行换算
        # newData = []
        # for i in range(len(data)):
        #     newDataRow = []
        #     for j in range(len(data[i])):
        #         strData = data[i][j]
        #         if strData == 'X':
        #             strData = '2'
        #         if strData == '/':
        #             strData = '1'
        #         newDataRow.append(strData)
        #     newData.append(newDataRow)
        # print(newData)

        #  获取表格的行列表头
        hHeaders = df_list[0][2:]
        vHeaders = [df_list[i][0] for i in range(2, self.tableWidget.rowCount())]
        # 　转化为DataFrame
        self.df = pandas.DataFrame(data, columns=hHeaders)
        self.df.index = vHeaders
        self.setHeaderText(hHeaders, vHeaders)
        #print(self.df)

    # 新增一行
    def newRow(self, row, col):
        self.rowNumber = self.rowNumber + 1
        self.tableWidget.insertRow(row + 1)  # 表格中插入行

        # # df indexing is slow, so use lists
        # list 保存所有值
        df_list = []
        for row in range(self.tableWidget.rowCount()):
            df_list2 = []
            for col in range(self.tableWidget.columnCount()):
                table_item = self.tableWidget.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        #print(df_list)
        # 表头
        hHeaders = df_list[0][2:]
        #print(hHeaders)
        vHeaders = [df_list[i][0] for i in range(2, self.tableWidget.rowCount())]
        #print(vHeaders)
        #
        rowNum = self.rowNumber + 2
        colNum = self.colNumber + 2
        # 重新刷新表格数值
        for i in range(0, rowNum):
            for j in range(0, colNum):
                str1 = str(df_list[i][j])
                itemNew = QTableWidgetItem(str1)
                if str1 is '/' or str1 is 'X':
                    itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                else:
                    itemNew.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, itemNew)
        # 重新设定表格格式
        self.initTable()
        self.setHeaderText(hHeaders, vHeaders)

    # 删除列
    def delRow(self, row, col):
        #  删除
        if self.rowNumber == 1:
            return
        self.rowNumber = self.rowNumber - 1
        self.tableWidget.removeRow(row)

        df_list = []
        for row in range(self.tableWidget.rowCount()):
            df_list2 = []
            for col in range(self.tableWidget.columnCount()):
                table_item = self.tableWidget.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        #print(df_list)

        hHeaders = df_list[0][2:]
        #print(hHeaders)
        vHeaders = [df_list[i][0] for i in range(2, self.tableWidget.rowCount())]
        #print(vHeaders)

        rowNum = self.rowNumber + 2
        colNum = self.colNumber + 2
        # 赋值item 并且刷新
        for i in range(2, rowNum):
            for j in range(2, colNum):
                str1 = str(df_list[i][j])
                itemNew = QTableWidgetItem(str1)
                #itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                self.tableWidget.setItem(i, j, itemNew)
        self.initTable()
        self.setHeaderText(hHeaders, vHeaders)

    # 新增列
    def newCol(self, row, col):
        # 新增一行
        self.colNumber = self.colNumber + 1
        self.tableWidget.insertColumn(col + 1)

        # # df indexing is slow, so use lists
        df_list = []
        for row in range(self.tableWidget.rowCount()):
            df_list2 = []
            for col in range(self.tableWidget.columnCount()):
                table_item = self.tableWidget.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        #print(df_list)
        #
        hHeaders = df_list[0][2:]
        #print(hHeaders)
        vHeaders = [df_list[i][0] for i in range(2, self.tableWidget.rowCount())]
        #print(vHeaders)
        #
        rowNum = self.rowNumber + 2
        colNum = self.colNumber + 2
        # 赋值item 并且刷新
        for i in range(0, rowNum):
            for j in range(0, colNum):
                str1 = str(df_list[i][j])
                itemNew = QTableWidgetItem(str1)
                if str1 is '/' or str1 is 'X':
                    itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                else:
                    itemNew.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, itemNew)

        self.initTable()
        self.setHeaderText(hHeaders, vHeaders)

    # 删除列
    def delCol(self, row, col):
        #  删除
        if self.colNumber == 1:
            return
        self.colNumber = self.colNumber - 1
        self.tableWidget.removeColumn(col)

        df_list = []
        for row in range(self.tableWidget.rowCount()):
            df_list2 = []
            for col in range(self.tableWidget.columnCount()):
                table_item = self.tableWidget.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)
        #print(df_list)

        hHeaders = df_list[0][2:]
        #print(hHeaders)
        vHeaders = [df_list[i][0] for i in range(2, self.tableWidget.rowCount())]
        #print(vHeaders)

        rowNum = self.rowNumber + 2
        colNum = self.colNumber + 2
        # 赋值item 并且刷新
        for i in range(2, rowNum):
            for j in range(2, colNum):
                str1 = str(df_list[i][j])
                itemNew = QTableWidgetItem(str1)
                #itemNew.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设定为居中
                self.tableWidget.setItem(i, j, itemNew)

        self.initTable()
        self.setHeaderText(hHeaders, vHeaders)
