import datetime
import sys

from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from python_gui_files import mainwindow, moduleSettings
import module
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import logging

logging.basicConfig(filename="logs/gui_logs.log", level=logging.INFO)
log = logging.getLogger("KeyError")


class WINDOW(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        """
        pyuic5 gui_files/mainwindow.ui -o python_gui_files/mainwindow.py
        """
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.module: module.Module = module.Module()

        # buttons connection
        self.newProjectButton.clicked.connect(self.__newProject)
        self.loadProjectButton.clicked.connect(self.__loadProject)
        self.saveProjectButton.clicked.connect(self.__saveProject)

        # -- Module settings --

        # adding module settings into the layout
        for item in self.module.settings["module"]["property"]:
            print(item)
            HLayout = QHBoxLayout()

            label = QLabel()
            label.setText(item)
            HLayout.addWidget(label, alignment=Qt.AlignCenter)

            lineEdit = QLineEdit()
            lineEdit.setText(self.module.settings["module"]["property"][item])
            HLayout.addWidget(lineEdit, alignment=Qt.AlignCenter)

            self.ModuleInfoSettingLayout.addLayout(HLayout)

        self.show()

    def __newProject(self):
        self.module = module.Module()

    def __loadProject(self):
        filename, ok = QFileDialog.getOpenFileName(self,
                                                   "Выберите файл",
                                                   ".",
                                                   "tcl(*.tcl);;json(*.json);;All Files(*.*)")
        self.module.read_file(filename)

    def __saveProject(self):
        root, fileType = QFileDialog.getSaveFileName(self, "save", "", "tcl(*.tcl);;json(*.json)")
        print(f"{root}  {fileType}")
        if fileType == "tcl(*.tcl)":
            self.module.write_to_tcl(filename=root)
        elif fileType == "json(*.json)":
            self.module.write_to_json(filename=root)
