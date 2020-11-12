# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mslib/msui/ui/ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MSSMainWindow(object):
    def setupUi(self, MSSMainWindow):
        MSSMainWindow.setObjectName("MSSMainWindow")
        MSSMainWindow.resize(442, 636)
        self.centralwidget = QtWidgets.QWidget(MSSMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listFlightTracks = QtWidgets.QListWidget(self.groupBox_3)
        self.listFlightTracks.setAlternatingRowColors(False)
        self.listFlightTracks.setTextElideMode(QtCore.Qt.ElideNone)
        self.listFlightTracks.setObjectName("listFlightTracks")
        self.verticalLayout_6.addWidget(self.listFlightTracks)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listViews = QtWidgets.QListWidget(self.groupBox)
        self.listViews.setObjectName("listViews")
        self.verticalLayout_4.addWidget(self.listViews)
        self.verticalLayout.addWidget(self.groupBox)
        self.labelStatusbar = QtWidgets.QLabel(self.centralwidget)
        self.labelStatusbar.setScaledContents(False)
        self.labelStatusbar.setObjectName("labelStatusbar")
        self.verticalLayout.addWidget(self.labelStatusbar)
        MSSMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MSSMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 20))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuImport_Flight_Track = QtWidgets.QMenu(self.menu_File)
        self.menuImport_Flight_Track.setObjectName("menuImport_Flight_Track")
        self.menuExport_Active_Flight_Track = QtWidgets.QMenu(self.menu_File)
        self.menuExport_Active_Flight_Track.setObjectName("menuExport_Active_Flight_Track")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Mscolab = QtWidgets.QMenu(self.menubar)
        self.menu_Mscolab.setObjectName("menu_Mscolab")
        MSSMainWindow.setMenuBar(self.menubar)
        self.action_Quit = QtWidgets.QAction(MSSMainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionNewFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionNewFlightTrack.setObjectName("actionNewFlightTrack")
        self.actionOpenFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionOpenFlightTrack.setObjectName("actionOpenFlightTrack")
        self.actionSaveActiveFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrack.setObjectName("actionSaveActiveFlightTrack")
        self.actionSaveActiveFlightTrackAs = QtWidgets.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrackAs.setObjectName("actionSaveActiveFlightTrackAs")
        self.actionCloseSelectedFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionCloseSelectedFlightTrack.setShortcut("")
        self.actionCloseSelectedFlightTrack.setObjectName("actionCloseSelectedFlightTrack")
        self.actionTopView = QtWidgets.QAction(MSSMainWindow)
        self.actionTopView.setObjectName("actionTopView")
        self.actionSideView = QtWidgets.QAction(MSSMainWindow)
        self.actionSideView.setObjectName("actionSideView")
        self.actionTableView = QtWidgets.QAction(MSSMainWindow)
        self.actionTableView.setObjectName("actionTableView")
        self.actionAboutMSUI = QtWidgets.QAction(MSSMainWindow)
        self.actionAboutMSUI.setObjectName("actionAboutMSUI")
        self.actionConfiguration = QtWidgets.QAction(MSSMainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionOnlineHelp = QtWidgets.QAction(MSSMainWindow)
        self.actionOnlineHelp.setObjectName("actionOnlineHelp")
        self.actionActivateSelectedFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionActivateSelectedFlightTrack.setShortcut("")
        self.actionActivateSelectedFlightTrack.setObjectName("actionActivateSelectedFlightTrack")
        self.actionMscolabProjects = QtWidgets.QAction(MSSMainWindow)
        self.actionMscolabProjects.setObjectName("actionMscolabProjects")
        self.menu_File.addAction(self.actionNewFlightTrack)
        self.menu_File.addAction(self.actionOpenFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionActivateSelectedFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionSaveActiveFlightTrack)
        self.menu_File.addAction(self.actionSaveActiveFlightTrackAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionCloseSelectedFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menuImport_Flight_Track.menuAction())
        self.menu_File.addAction(self.menuExport_Active_Flight_Track.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionConfiguration)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_View.addAction(self.actionTopView)
        self.menu_View.addAction(self.actionSideView)
        self.menu_View.addAction(self.actionTableView)
        self.menu_Help.addAction(self.actionOnlineHelp)
        self.menu_Help.addAction(self.actionAboutMSUI)
        self.menu_Mscolab.addAction(self.actionMscolabProjects)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Mscolab.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MSSMainWindow)
        self.action_Quit.triggered.connect(MSSMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MSSMainWindow)

    def retranslateUi(self, MSSMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MSSMainWindow.setWindowTitle(_translate("MSSMainWindow", "Mission Support System"))
        self.groupBox_3.setTitle(_translate("MSSMainWindow", "Open Flight Tracks:"))
        self.listFlightTracks.setToolTip(_translate("MSSMainWindow", "List of open flight tracks.\n"
"Double-click a flight track to activate it.\n"
"Save a flight track to name it."))
        self.groupBox.setTitle(_translate("MSSMainWindow", "Open Views:"))
        self.listViews.setToolTip(_translate("MSSMainWindow", "Double-click a view to bring it to the front."))
        self.labelStatusbar.setText(_translate("MSSMainWindow", "Status : "))
        self.menu_File.setTitle(_translate("MSSMainWindow", "&File"))
        self.menuImport_Flight_Track.setTitle(_translate("MSSMainWindow", "Import Flight Track"))
        self.menuExport_Active_Flight_Track.setTitle(_translate("MSSMainWindow", "Export Active Flight Track"))
        self.menu_View.setTitle(_translate("MSSMainWindow", "&Views"))
        self.menu_Help.setTitle(_translate("MSSMainWindow", "&Help"))
        self.menu_Mscolab.setTitle(_translate("MSSMainWindow", "&Mscolab"))
        self.action_Quit.setText(_translate("MSSMainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MSSMainWindow", "Ctrl+Q"))
        self.actionNewFlightTrack.setText(_translate("MSSMainWindow", "&New Flight Track"))
        self.actionNewFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+N"))
        self.actionOpenFlightTrack.setText(_translate("MSSMainWindow", "&Open Flight Track..."))
        self.actionOpenFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+O"))
        self.actionSaveActiveFlightTrack.setText(_translate("MSSMainWindow", "&Save Active Flight Track"))
        self.actionSaveActiveFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+S"))
        self.actionSaveActiveFlightTrackAs.setText(_translate("MSSMainWindow", "Save Active Flight Track &As..."))
        self.actionCloseSelectedFlightTrack.setText(_translate("MSSMainWindow", "&Close Selected Flight Track"))
        self.actionTopView.setText(_translate("MSSMainWindow", "&Top View (Horizontal Section)"))
        self.actionTopView.setShortcut(_translate("MSSMainWindow", "Ctrl+H"))
        self.actionSideView.setText(_translate("MSSMainWindow", "&Side View (Vertical Section)"))
        self.actionSideView.setShortcut(_translate("MSSMainWindow", "Ctrl+V"))
        self.actionTableView.setText(_translate("MSSMainWindow", "T&able View"))
        self.actionTableView.setShortcut(_translate("MSSMainWindow", "Ctrl+T"))
        self.actionAboutMSUI.setText(_translate("MSSMainWindow", "&About MSS"))
        self.actionConfiguration.setText(_translate("MSSMainWindow", "Configuration"))
        self.actionOnlineHelp.setText(_translate("MSSMainWindow", "Online &Help"))
        self.actionActivateSelectedFlightTrack.setText(_translate("MSSMainWindow", "Activate Selected Flight Track"))
        self.actionMscolabProjects.setText(_translate("MSSMainWindow", "Mscolab projects"))
