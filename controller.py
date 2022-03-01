from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import sys

from View import View
from Model import Model


class Controller(QMainWindow, View):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.model = Model()

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
        self.model.AddNumberValue(text)
        self.ShowValues()

    def AddOperatorPressed(self, text):
        self.model.AddOperator(text)
        self.ShowValues()

    def NegativeAndPositiveSwitchPressed(self):
        self.model.NegativeAndPositiveSwitch()
        self.ShowValues()

    def TypePercentagePressed(self):
        self.model.TypePercentage()
        self.ShowValues()

    def MakeFloatPressed(self):
        self.model.MakeFloat()
        self.ShowValues()

    def RemoveTypingLastCharPressed(self):
        self.model.RemoveTypingLastCharactor()
        self.ShowValues()

    def ClearDisplayPressed(self):
        print("clear data")
        self.model.ClearData()
        self.ShowValues()

    def CalculatePressed(self):
        self.model.Calculate()
        self.ShowValues()

    def ShowValues(self):
        self.previousValueLineEdit.setText(self.model.displayValues[0])
        self.currentValueLineEdit.setText(self.model.displayValues[1])
