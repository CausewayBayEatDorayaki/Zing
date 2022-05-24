from PySide2.QtCore import QObject, Signal


class LoadSignal(QObject):
    Signal = Signal(str)  # 信号

    def __init__(self, parent=None):
        super().__init__(parent)

    def send(self, torf):
        self.Signal.emit(torf)


class CheckerSignal(QObject):
    Signal = Signal(str)  # 信号

    def __init__(self, parent=None):
        super().__init__(parent)

    def send(self, txt):
        self.Signal.emit(txt)
