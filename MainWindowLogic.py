from qtpy import QtWidgets

import sys

from MainWindow import Ui_MainWindow


class MainWindowLogic(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, viewModel, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.viewModel = viewModel

        self.numButtons = [self.num0Button, self.num1Button, self.num2Button, self.num3Button,
                           self.num4Button, self.num5Button, self.num6Button, self.num7Button, self.num8Button, self.num9Button]

        self.operatorButtons = [
            self.opeMultiplyButton, self.opeDevideButton, self.opePlusButton, self.opeMinusButton]

        for i in range(len(self.numButtons)):
            buttonValue = self.numButtons[i].text()
            self.numButtons[i].clicked.connect(
                lambda ch, text=buttonValue: self.AddNumberValuePressed(text))

        for i in range(len(self.operatorButtons)):
            buttonOperator = self.operatorButtons[i].text()
            self.operatorButtons[i].clicked.connect(
                lambda ch, text=buttonOperator: self.AddOperatorPressed(text))

        self.clearButton.clicked.connect(lambda _: self.ClearDisplayPressed())

        self.negPosSwitcherButton.clicked.connect(
            lambda _: self.NegativeAndPositiveSwitchPressed())

        self.getPercentButton.clicked.connect(
            lambda _: self.TypePercentagePressed())

        self.makeFloatButton.clicked.connect(lambda _: self.MakeFloatPressed())

        self.removeLastNumButton.clicked.connect(
            lambda _: self.RemoveTypingLastCharPressed())

        self.calculateButton.clicked.connect(lambda _: self.CalculatePressed())

        self.actionExit.triggered.connect(lambda _: sys.exit())

    def AddNumberValuePressed(self, text):
        self.viewModel.AddNumberValue(text)
        self.ShowValues()

    def AddOperatorPressed(self, text):
        self.viewModel.AddOperator(text)
        self.ShowValues()

    def NegativeAndPositiveSwitchPressed(self):
        self.viewModel.NegativeAndPositiveSwitch()
        self.ShowValues()

    def TypePercentagePressed(self):
        self.viewModel.TypePercentage()
        self.ShowValues()

    def MakeFloatPressed(self):
        self.viewModel.MakeFloat()
        self.ShowValues()

    def RemoveTypingLastCharPressed(self):
        self.viewModel.RemoveTypingLastCharactor()
        self.ShowValues()

    def ClearDisplayPressed(self):
        print("clear data")
        self.viewModel.ClearData()
        self.ShowValues()

    def CalculatePressed(self):
        self.viewModel.Calculate()
        self.ShowValues()

    def ShowValues(self):
        self.previousValueLineEdit.setText(self.viewModel.displayValues[0])
        self.currentValueLineEdit.setText(self.viewModel.displayValues[1])
