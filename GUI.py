import datetime
import sys

from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from python_gui_files import mainwindow, moduleSettings
import module


class WINDOW(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        """
        pyuic5 gui_files/mainwindow.ui -o python_gui_files/mainwindow.py
        pyuic5 gui_files/moduleSettings.ui -o python_gui_files/moduleSettings.py


        """
        super().__init__()
        self.module: module.Module = module.Module()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.newProjectButton.clicked.connect(self.__newProject)
        self.loadProjectButton.clicked.connect(self.__loadProject)
        self.moduleSettingsButton.clicked.connect(self.__moduleSettings)
        self.moduleFilesetButton.clicked.connect(self.__moduleFileset)
        self.show()


"""
    def __newProject(self):
        self.module = module.Module()

    def __loadProject(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "JSON Files(*.json);;TCL Files(*.tcl);;All Files(*)")
        self.module.read_file(filename)

    def __save_module_settings(self):
        global moduleSettingsData, textEditsForModuleSettings
        for prop, prop2 in zip(moduleSettingsData, textEditsForModuleSettings):
            moduleSettingsData[prop] = prop2.toPlainText() if prop2.toPlainText() else None

        print(moduleSettingsData)
        self.module.settings['module']['property'].update(
            moduleSettingsData
        )
        self.windowForWidgets = QtWidgets.QWidget(self.CurrentProjectLayout)
        self.windowForWidgets.setGeometry(QtCore.QRect(0, 50, 1281, 591))
        self.windowForWidgets.setObjectName("windowForWidgets")
        del moduleSettingsData, textEditsForModuleSettings

    def __moduleSettings(self):
        print("__moduleSettings")
        moduleSettingsForm = QFormLayout(self.windowForWidgets)

        global moduleSettingsData
        moduleSettingsData = {

        }

        global textEditsForModuleSettings
        textEditsForModuleSettings = []

        for prop in self.module.settings['module']['property']:
            label = QLabel(text=prop)
            textEdit = QTextEdit()
            textEditsForModuleSettings.append(textEdit)
            moduleSettingsData.update(
                {
                    prop: None
                }
            )

            moduleSettingsForm.addWidget(label)
            moduleSettingsForm.addWidget(textEdit)

        saveModuleSettings = QtWidgets.QPushButton(text="save project")
        moduleSettingsForm.addWidget(saveModuleSettings)
        saveModuleSettings.clicked.connect(self.__save_module_settings)

    def __moduleFileset(self):

        global moduleFilesetQSYNTHData
        moduleFilesetQSYNTHData = {

        }

        global textEditsForModuleQSYNTHFileset
        textEditsForModuleQSYNTHFileset = []

        moduleFilesetForm = QFormLayout(self.windowForWidgets)



        for prop in self.module.settings["fileset"]["QUARTUS_SYNTH"]["property"]:
            label = QLabel(text=prop)
            textEdit = QTextEdit()
            textEditsForModuleQSYNTHFileset.append(textEdit)
            moduleFilesetQSYNTHData.update(
                {
                    prop: None
                }
            )
            moduleFilesetForm.addWidget(label)
            moduleFilesetForm.addWidget(textEdit)

        for file in self.module.settings["fileset"]["files"]:
            print(file)
"""