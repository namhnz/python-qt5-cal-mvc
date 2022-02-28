from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import sys

from View import View
from Model import Model;


class Controller(QMainWindow, View):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.model = Model();

        self.numButtons = [self.num0Button, self.num1Button, self.num2Button, self.num3Button,
                           self.num4Button, self.num5Button, self.num6Button, self.num7Button, self.num8Button, self.num9Button]

        self.operatorButtons = [self.opeMultiplyButton, self.opeDevideButton, self.opePlusButton, self.opeMinusButton];

        for i in range(len(self.numButtons)):
            buttonValue = self.numButtons[i].text()
            self.numButtons[i].clicked.connect(
                lambda ch, text=buttonValue: self.model.AddNumberValue(text))

        for i in range(len(self.operatorButtons)):
            buttonOperator = self.operatorButtons[i].text();
            self.operatorButtons[i].clicked.connect(lambda ch, text=buttonOperator: self.model.AddOperator(text));

        self.clearButton.clicked.connect(lambda ch: self.ClearDisplay());

        self.calculateButton.clicked.connect(lambda ch: self.model.Calculate());

    def ClearDisplay(self):
        print("clear data");
        self.model.ClearData();