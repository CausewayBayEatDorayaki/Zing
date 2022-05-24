class Stack:
    def __init__(self):
        self.lst = []  # 存放数据的列表
        self.top = 0  # 栈顶指针
    # 入栈
    def push(self, el):
        self.lst.insert(self.top, el)  # 放元素
        self.top += 1  # 栈顶指针向上移动一下
    # 出栈
    def pop(self):
        self.top -= 1
        el = self.lst[self.top]
        self.lst.pop(self.top)
        return el

