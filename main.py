# coding: UTF-8
import module
import sys
import GUI
from PyQt5.QtWidgets import QApplication

def do_smth():
    app = QApplication(sys.argv)
    ex = GUI.WINDOW()
    sys.exit(app.exec_())



if __name__ == "__main__":
    do_smth()
