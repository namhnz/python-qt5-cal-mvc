class Model:
    def __init__(self) -> None:
        self.leftSideValue = ""
        self.rightSideValue = ""
        self.waitingOperator = ""
        self.displayValues = ["", ""]

    def AddNumberValue(self, num):
        if "=" in self.displayValues[0]:
            self.ClearData()

        if not self.waitingOperator:
            self.leftSideValue += num
            self.displayValues = ["", self.leftSideValue]
        else:
            self.rightSideValue += num
            self.displayValues = [self.leftSideValue +
                                  self.waitingOperator, self.rightSideValue]

    def RemoveTypingLastCharactor(self):
        if not self.waitingOperator:
            self.leftSideValue = self.leftSideValue[:-1]
            self.displayValues = ["", self.leftSideValue]
        else:
            self.rightSideValue = self.rightSideValue[:-1]
            self.displayValues = [self.leftSideValue +
                                  self.waitingOperator, self.rightSideValue]

    def NegativeAndPositiveSwitch(self):
        if not self.waitingOperator:
            # Neu gia tri dang nhap khac empty hoac 0 thi tien hanh them bot dau tru
            if self.leftSideValue and self.leftSideValue != "0":
                self.leftSideValue = "-" + \
                    self.leftSideValue if not self.leftSideValue.startswith(
                        "-") else self.leftSideValue[1:]
                self.displayValues = ["", self.leftSideValue]
        else:
            if self.rightSideValue and self.rightSideValue != "0":
                self.rightSideValue = "-" + \
                    self.rightSideValue if not self.rightSideValue.startswith(
                        "-") else self.rightSideValue[1:]
                self.displayValues = [self.leftSideValue +
                                      self.waitingOperator, self.rightSideValue]

    def AddOperator(self, operator):
        if self.waitingOperator:
            result = eval(self.leftSideValue +
                          self.waitingOperator + self.rightSideValue)
            self.leftSideValue = str(result)
            self.rightSideValue = ""

        self.waitingOperator = operator
        self.displayValues = [self.leftSideValue + self.waitingOperator, ""]

    def TypePercentage(self):
        if not self.waitingOperator:
            result = eval(self.leftSideValue + "/100")
            self.leftSideValue = str(result)
            self.displayValues = ["", self.leftSideValue]
        else:
            result = eval(self.rightSideValue + "/100")
            self.rightSideValue = str(result)
            self.displayValues = [self.leftSideValue +
                                  self.waitingOperator, self.rightSideValue]

    def MakeFloat(self):
        if "=" in self.displayValues[0]:
            self.ClearData()

        if not self.waitingOperator:
            if self.leftSideValue:
                self.leftSideValue += "." if "." not in self.leftSideValue else ""
            else:
                self.leftSideValue = "0."
            self.displayValues = ["", self.leftSideValue]
        else:
            if self.rightSideValue:
                self.rightSideValue += "." if "." not in self.rightSideValue else ""
            else:
                self.rightSideValue = "0."
            self.displayValues = [self.leftSideValue +
                                  self.waitingOperator, self.rightSideValue]

    def Calculate(self):
        result = eval(self.leftSideValue +
                      self.waitingOperator + self.rightSideValue)
        self.displayValues = [
            self.leftSideValue + self.waitingOperator + self.rightSideValue + "=", str(result)]

        self.leftSideValue = str(result)
        self.rightSideValue = ""
        self.waitingOperator = ""

    def ClearData(self):
        self.leftSideValue = ""
        self.rightSideValue = ""
        self.waitingOperator = ""
        self.displayValues = ["", ""]
