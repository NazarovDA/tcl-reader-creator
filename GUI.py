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
        terminal command that using for convert .ui -> .py
        pyuic5 gui_files/mainwindow.ui -o python_gui_files/mainwindow.py
        """
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.module: module.Module = module.Module()

        self.PARAMSLABEL = []
        self.LINEEDIT = []
        # -- Module settings --
        self.moduleSettingsLineEdits = []
        self.done_module_settings = False
        self.__show_module_settings()

        # -- Fileset settings
        self.QSLineEdits = []
        self.__show_fileset()

        # -- Parameters settings

        self.parameters = {}
        self.__show_parameters()

        # buttons connection
        self.newProjectButton.clicked.connect(self.__newProject)
        self.loadProjectButton.clicked.connect(self.__loadProject)
        self.saveProjectButton.clicked.connect(self.__saveProject)
        self.saveModuleSettingsButton.clicked.connect(self.__save_module_settings)
        self.SaveFilesetButton.clicked.connect(self.__save_fileset)
        self.AddFileToFilesetButton.clicked.connect(self.__add_file_to_fileset)
        self.addParameterButton.clicked.connect(self.__add_parameter)

        self.show()

    # -- module settings --
    def __save_module_settings(self):
        for prop, newProp in zip(self.module.settings["module"]["property"], self.moduleSettingsLineEdits):
            self.module.settings["module"]["property"][prop] = newProp

    def __show_module_settings(self):
        # adding module settings into the layout
        if self.done_module_settings is False:
            self.labels = []
            for item in self.module.settings["module"]["property"]:
                HLayout = QHBoxLayout()

                label = QLabel()
                label.setText(item)
                self.labels.append(label)
                HLayout.addWidget(label, alignment=Qt.AlignCenter)

                lineEdit = QLineEdit()
                lineEdit.setText(self.module.settings["module"]["property"][item])
                self.moduleSettingsLineEdits.append(lineEdit)
                HLayout.addWidget(lineEdit, alignment=Qt.AlignCenter)

                self.ModuleInfoSettingLayout.addLayout(HLayout)
            self.done_module_settings = True

        elif self.done_module_settings:
            for lineEdit, value in zip(self.moduleSettingsLineEdits, self.module.settings["module"]["property"]):
                lineEdit.setText(self.module.settings["module"]["property"][value])

    # -- fileset settings --
    def __save_fileset(self):
        for prop, newProp in zip(self.module.settings['fileset']['QUARTUS_SYNTH']['property'], self.QSLineEdits):
            self.module.settings['fileset']['QUARTUS_SYNTH']['property'][prop] = newProp.text

        for file in self.module.settings['fileset']["files"]:
            if file != self.module.settings['fileset']['QUARTUS_SYNTH']['property']["TOP_LEVEL"]:
                self.module.settings['fileset']["files"][file]["status"] = None
            else:
                self.module.settings['fileset']["files"][file]["status"] = "TOP_LEVEL"

    def __add_file_to_fileset(self):
        filename, ok = QFileDialog.getOpenFileName(self,
                                                   "Выберите файл",
                                                   ".",
                                                   "sv(*.sv);;All Files(*.*)")
        try:
            a = self.module.settings['fileset']['files'][filename]
        except KeyError:
            newDict = self.module.settings['fileset']['files'][filename.split("/")[-1]] = {}
            newDict.update(
                {
                    "type": "SYSTEM_VERILOG",
                    "PATH": filename,
                    "status": None
                }
            )
            self.__show_fileset()

    def __add_file_headlines(self):
        HLayout = QHBoxLayout()
        label1 = QLabel()
        label1.setText("type")
        label2 = QLabel()
        label2.setText("path")
        label3 = QLabel()
        label3.setText("name")
        HLayout.addWidget(label1, alignment=Qt.AlignCenter)
        HLayout.addWidget(label2, alignment=Qt.AlignCenter)
        HLayout.addWidget(label3, alignment=Qt.AlignCenter)
        self.FilesVLayout.addLayout(HLayout)

    def __show_fileset(self):
        # file list

        while self.FilesVLayout.count():
            sublayout = self.FilesVLayout.takeAt(0).layout()
            while sublayout.count():
                widget: QtWidgets = sublayout.takeAt(0).widget()
                widget.setParent(None)

        while self.FileSettingQSYNTH.children():
            sublayout = self.FileSettingQSYNTH.takeAt(0).layout()
            while sublayout.count():
                widget: QtWidgets = sublayout.takeAt(0).widget()
                widget.setParent(None)

        for QSYNTHProp in self.module.settings['fileset']['QUARTUS_SYNTH']['property']:
            HLayout = QHBoxLayout()

            label = QLabel()
            label.setText(QSYNTHProp)
            HLayout.addWidget(label, alignment=Qt.AlignCenter)
            lineEdit = QLineEdit()
            lineEdit.setText(self.module.settings['fileset']['QUARTUS_SYNTH']['property'][QSYNTHProp])
            self.QSLineEdits.append(lineEdit)
            HLayout.addWidget(lineEdit, alignment=Qt.AlignCenter)

            self.FileSettingQSYNTH.addLayout(HLayout)

        self.__add_file_headlines()
        for file in self.module.settings['fileset']['files']:
            HLayout = QHBoxLayout()

            typeLabel = QLabel()
            typeLabel.setText(self.module.settings['fileset']['files'][file]['type'])
            HLayout.addWidget(typeLabel, alignment=Qt.AlignCenter)

            pathLabel = QLabel()
            pathLabel.setText(self.module.settings['fileset']['files'][file]['PATH'])
            HLayout.addWidget(pathLabel, alignment=Qt.AlignCenter)

            nameLabel = QLabel()
            nameLabel.setText(file)
            HLayout.addWidget(nameLabel, alignment=Qt.AlignCenter)

            self.FilesVLayout.addLayout(HLayout)

    # -- parameters settings --
    def __add_parameter(self):
        name, ok = QInputDialog.getText(self, "Input dialog", "Input parameter name")
        newDict = {
            name: {
                "property": {
                    "DEFAULT_VALUE": None,
                    "DISPLAY_NAME": None,
                    "TYPE": None,
                    "UNITS": None,
                    "HDL_PARAMETER": None
                }
            }
        }
        self.module.settings["parameter"].update(newDict)
        self.__show_parameters()

    def __save_parameters(self):
        pass

    def __show_parameters(self):

        while len(self.PARAMSLABEL) > 0:
            label: QLabel = self.PARAMSLABEL.pop(0)
            label.setParent(None)
        while len(self.LINEEDIT) > 0:
            lineEdit: QLineEdit = self.LINEEDIT.pop(0)
            lineEdit.setParent(None)

        for parameter in self.module.settings['parameter']:
            self.parameters[parameter] = []
            HParamLayout = QVBoxLayout()
            name = QLabel()
            name.setText(parameter)
            self.PARAMSLABEL.append(name)
            HParamLayout.addWidget(name)
            for info in self.module.settings['parameter'][parameter]['property']:
                HLayout = QHBoxLayout()
                label = QLabel()
                label.setText(info)
                self.PARAMSLABEL.append(label)
                HLayout.addWidget(label)
                lineEdit = QLineEdit()
                lineEdit.setText(self.module.settings['parameter'][parameter]['property'][info])
                self.LINEEDIT.append(lineEdit)
                HLayout.addWidget(lineEdit)
                self.parameters[parameter].append(lineEdit)
                HParamLayout.addLayout(HLayout)
            self.ParametersLayout.addLayout(HParamLayout)

    # -- сonnection point settings --
    def __show_connection_points(self):
        # TODO: Figure out how to add connection points properly
        scrollaAreaWidget = QWidget()
        for interface in self.module.settings["interface"]:
            pass


    # -- project settings --
    def __newProject(self):
        self.module = module.Module()
        self.__show_module_settings()
        self.__show_fileset()
        self.__show_parameters()

    def __loadProject(self):
        filename, ok = QFileDialog.getOpenFileName(self,
                                                   "Выберите файл",
                                                   ".",
                                                   "tcl(*.tcl);;json(*.json);;All Files(*.*)")
        self.module.read_file(filename)

        self.__show_parameters()
        self.__show_module_settings()
        self.__show_fileset()

    def __saveProject(self):
        root, fileType = QFileDialog.getSaveFileName(self, "save", "", "tcl(*.tcl);;json(*.json)")
        if fileType == "tcl(*.tcl)":
            self.module.write_to_tcl(filename=root)
        elif fileType == "json(*.json)":
            self.module.write_to_json(filename=root)
