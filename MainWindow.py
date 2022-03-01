# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.previousValueLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.previousValueLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previousValueLineEdit.setReadOnly(True)
        self.previousValueLineEdit.setObjectName("previousValueLineEdit")
        self.verticalLayout.addWidget(self.previousValueLineEdit)
        self.currentValueLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.currentValueLineEdit.setFont(font)
        self.currentValueLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentValueLineEdit.setReadOnly(True)
        self.currentValueLineEdit.setObjectName("currentValueLineEdit")
        self.verticalLayout.addWidget(self.currentValueLineEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.getPercentButton = QtWidgets.QPushButton(self.centralwidget)
        self.getPercentButton.setObjectName("getPercentButton")
        self.horizontalLayout_6.addWidget(self.getPercentButton)
        self.negPosSwitcherButton = QtWidgets.QPushButton(self.centralwidget)
        self.negPosSwitcherButton.setObjectName("negPosSwitcherButton")
        self.horizontalLayout_6.addWidget(self.negPosSwitcherButton)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.removeLastNumButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeLastNumButton.setObjectName("removeLastNumButton")
        self.horizontalLayout_6.addWidget(self.removeLastNumButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.num7Button = QtWidgets.QPushButton(self.centralwidget)
        self.num7Button.setObjectName("num7Button")
        self.horizontalLayout_5.addWidget(self.num7Button)
        self.num8Button = QtWidgets.QPushButton(self.centralwidget)
        self.num8Button.setObjectName("num8Button")
        self.horizontalLayout_5.addWidget(self.num8Button)
        self.num9Button = QtWidgets.QPushButton(self.centralwidget)
        self.num9Button.setObjectName("num9Button")
        self.horizontalLayout_5.addWidget(self.num9Button)
        self.opeMultiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.opeMultiplyButton.setObjectName("opeMultiplyButton")
        self.horizontalLayout_5.addWidget(self.opeMultiplyButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.num4Button = QtWidgets.QPushButton(self.centralwidget)
        self.num4Button.setObjectName("num4Button")
        self.horizontalLayout_4.addWidget(self.num4Button)
        self.num5Button = QtWidgets.QPushButton(self.centralwidget)
        self.num5Button.setObjectName("num5Button")
        self.horizontalLayout_4.addWidget(self.num5Button)
        self.num6Button = QtWidgets.QPushButton(self.centralwidget)
        self.num6Button.setObjectName("num6Button")
        self.horizontalLayout_4.addWidget(self.num6Button)
        self.opeMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.opeMinusButton.setObjectName("opeMinusButton")
        self.horizontalLayout_4.addWidget(self.opeMinusButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.num1Button = QtWidgets.QPushButton(self.centralwidget)
        self.num1Button.setObjectName("num1Button")
        self.horizontalLayout_3.addWidget(self.num1Button)
        self.num2Button = QtWidgets.QPushButton(self.centralwidget)
        self.num2Button.setObjectName("num2Button")
        self.horizontalLayout_3.addWidget(self.num2Button)
        self.num3Button = QtWidgets.QPushButton(self.centralwidget)
        self.num3Button.setObjectName("num3Button")
        self.horizontalLayout_3.addWidget(self.num3Button)
        self.opePlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.opePlusButton.setObjectName("opePlusButton")
        self.horizontalLayout_3.addWidget(self.opePlusButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.num0Button = QtWidgets.QPushButton(self.centralwidget)
        self.num0Button.setObjectName("num0Button")
        self.horizontalLayout.addWidget(self.num0Button)
        self.makeFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.makeFloatButton.setObjectName("makeFloatButton")
        self.horizontalLayout.addWidget(self.makeFloatButton)
        self.opeDevideButton = QtWidgets.QPushButton(self.centralwidget)
        self.opeDevideButton.setObjectName("opeDevideButton")
        self.horizontalLayout.addWidget(self.opeDevideButton)
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setObjectName("calculateButton")
        self.horizontalLayout.addWidget(self.calculateButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getPercentButton.setText(_translate("MainWindow", "%"))
        self.negPosSwitcherButton.setText(_translate("MainWindow", "+/-"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.removeLastNumButton.setText(_translate("MainWindow", "<="))
        self.num7Button.setText(_translate("MainWindow", "7"))
        self.num8Button.setText(_translate("MainWindow", "8"))
        self.num9Button.setText(_translate("MainWindow", "9"))
        self.opeMultiplyButton.setText(_translate("MainWindow", "*"))
        self.num4Button.setText(_translate("MainWindow", "4"))
        self.num5Button.setText(_translate("MainWindow", "5"))
        self.num6Button.setText(_translate("MainWindow", "6"))
        self.opeMinusButton.setText(_translate("MainWindow", "-"))
        self.num1Button.setText(_translate("MainWindow", "1"))
        self.num2Button.setText(_translate("MainWindow", "2"))
        self.num3Button.setText(_translate("MainWindow", "3"))
        self.opePlusButton.setText(_translate("MainWindow", "+"))
        self.num0Button.setText(_translate("MainWindow", "0"))
        self.makeFloatButton.setText(_translate("MainWindow", "."))
        self.opeDevideButton.setText(_translate("MainWindow", "/"))
        self.calculateButton.setText(_translate("MainWindow", "="))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))