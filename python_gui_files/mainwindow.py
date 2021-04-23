# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_files/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 320, 25))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ProjectLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.ProjectLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ProjectLayout.setContentsMargins(0, 0, 0, 0)
        self.ProjectLayout.setObjectName("ProjectLayout")
        self.newProjectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.newProjectButton.setObjectName("newProjectButton")
        self.ProjectLayout.addWidget(self.newProjectButton)
        self.saveProjectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveProjectButton.setObjectName("saveProjectButton")
        self.ProjectLayout.addWidget(self.saveProjectButton)
        self.loadProjectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loadProjectButton.setObjectName("loadProjectButton")
        self.ProjectLayout.addWidget(self.loadProjectButton)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(-4, 29, 1281, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.moduleProperties = QtWidgets.QWidget()
        self.moduleProperties.setObjectName("moduleProperties")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.moduleProperties)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.moduleVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.moduleVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.moduleVerticalLayout.setObjectName("moduleVerticalLayout")
        self.ModuleInfoSettingLayout = QtWidgets.QVBoxLayout()
        self.ModuleInfoSettingLayout.setObjectName("ModuleInfoSettingLayout")
        self.moduleVerticalLayout.addLayout(self.ModuleInfoSettingLayout)
        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        self.saveModuleSettingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveModuleSettingsButton.setObjectName("saveModuleSettingsButton")
        self.ButtonLayout.addWidget(self.saveModuleSettingsButton)
        self.moduleVerticalLayout.addLayout(self.ButtonLayout)
        self.tabWidget.addTab(self.moduleProperties, "")
        self.FilesetSettings = QtWidgets.QWidget()
        self.FilesetSettings.setObjectName("FilesetSettings")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.FilesetSettings)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, -1, 1281, 611))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.FileSetVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.FileSetVLayout.setContentsMargins(0, 0, 0, 0)
        self.FileSetVLayout.setObjectName("FileSetVLayout")
        self.FileSettingQSYNTH = QtWidgets.QVBoxLayout()
        self.FileSettingQSYNTH.setObjectName("FileSettingQSYNTH")
        self.FileSetVLayout.addLayout(self.FileSettingQSYNTH)
        self.FilesList = QtWidgets.QListView(self.verticalLayoutWidget_4)
        self.FilesList.setObjectName("FilesList")
        self.FileSetVLayout.addWidget(self.FilesList)
        self.ButtonsFileset = QtWidgets.QHBoxLayout()
        self.ButtonsFileset.setObjectName("ButtonsFileset")
        self.AddFileToFilesetButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.AddFileToFilesetButton.setObjectName("AddFileToFilesetButton")
        self.ButtonsFileset.addWidget(self.AddFileToFilesetButton)
        self.SaveFilesetButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.SaveFilesetButton.setObjectName("SaveFilesetButton")
        self.ButtonsFileset.addWidget(self.SaveFilesetButton)
        self.FileSetVLayout.addLayout(self.ButtonsFileset)
        self.tabWidget.addTab(self.FilesetSettings, "")
        self.ParametersSettings = QtWidgets.QWidget()
        self.ParametersSettings.setObjectName("ParametersSettings")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.ParametersSettings)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, -1, 1281, 621))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.ParametersSettingVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.ParametersSettingVLayout.setContentsMargins(0, 0, 0, 0)
        self.ParametersSettingVLayout.setObjectName("ParametersSettingVLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.ParametersSettingVLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ParametersSettingsSaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.ParametersSettingsSaveButton.setObjectName("ParametersSettingsSaveButton")
        self.horizontalLayout_3.addWidget(self.ParametersSettingsSaveButton)
        self.ParametersSettingVLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.ParametersSettings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newProjectButton.setText(_translate("MainWindow", "New Project"))
        self.saveProjectButton.setText(_translate("MainWindow", "Save Project"))
        self.loadProjectButton.setText(_translate("MainWindow", "Load Project"))
        self.saveModuleSettingsButton.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.moduleProperties), _translate("MainWindow", "Module Settings"))
        self.AddFileToFilesetButton.setText(_translate("MainWindow", "Добавить файл"))
        self.SaveFilesetButton.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FilesetSettings), _translate("MainWindow", "Fileset"))
        self.ParametersSettingsSaveButton.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ParametersSettings), _translate("MainWindow", "Parameters"))
