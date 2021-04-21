import datetime
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from python_gui_files import mainwindow
import module


class WINDOW(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.module: module.Module = module.Module()
        self.setupUi(self)
        self.newProjectButton.clicked.connect(self.__newProject)
        self.loadProjectButton.clicked.connect(self.__loadProject)

        self.show()

    def __newProject(self):
        self.module = module.Module()

    def __loadProject(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "JSON Files(*.json);;TCL Files(*.tcl);;All Files(*)")
        self.module.read_file(filename)
