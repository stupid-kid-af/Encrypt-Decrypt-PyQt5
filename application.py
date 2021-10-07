import sys
import os
import ui.template as template
from PyQt5 import QtWidgets, QtCore
from cipher import FileCipher


class Application(QtWidgets.QMainWindow, template.Ui_Window):

    path = '/'

    def __init__(self):
        super().__init__()  # Access to super/parent methods and options
        self.setupUi(self)  # Template init
        self.drop()
        self.encryptBtn.clicked.connect(self.encrypt)
        self.decryptBtn.clicked.connect(self.decrypt)

    def drop(self):
        self.DragDrop.installEventFilter(self)
        self.DragDrop.acceptDrops()
        self.DragDrop.setDragEnabled(True)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.DragEnter:
            if event.mimeData().hasFormat('text/plain'):
                event.accept()
                return True
        if event.type() == QtCore.QEvent.Drop:
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                if os.path.isfile(path):
                    self.path = path
            source.setText(os.path.basename(self.path))
            return True
        return False

    def encrypt(self):
        cipher = FileCipher(self.path, self.passphrase.text())
        cipher.encrypt()

    def decrypt(self):
        cipher = FileCipher(self.path, self.passphrase.text())
        cipher.decrypt()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
