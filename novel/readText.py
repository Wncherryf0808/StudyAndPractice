import sys
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QTextEdit, QWidget, QVBoxLayout


class Worker(QThread):
    update_signal = Signal(str)

    def run(self):
        with open('./douluo.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                self.update_signal.emit(line)
                time.sleep(0.01)


class ReadWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("readStory")

        self.qWidget = QWidget()
        self.setCentralWidget(self.qWidget)
        self.layout = QVBoxLayout(self.qWidget)

        self.textEdit = QTextEdit(self)
        self.layout.addWidget(self.textEdit)

        self.textEdit.resize(self.width(), self.height())
        self.worker = Worker()
        self.worker.update_signal.connect(self.update_text)
        self.worker.start()

    def update_text(self, text):
        self.textEdit.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    read = ReadWindow()
    read.show()
    sys.exit(app.exec())