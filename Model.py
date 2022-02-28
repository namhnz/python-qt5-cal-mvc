class Model:
    def __init__(self) -> None:
        self.leftSideValue = "";
        self.rightSideValue = "";
        self.waitingOperator = "";
        

    def AddNumberValue(self, num):

        if not self.waitingOperator:
            self.leftSideValue += num;
        else:
            self.rightSideValue += num;
        

    def AddOperator(self, operator):
        if self.waitingOperator:
            result = eval(self.leftSideValue + self.waitingOperator + self.rightSideValue);
            print(result);
            self.leftSideValue = str(result);
            self.rightSideValue = "";
        
        self.waitingOperator = operator;
           

    def Calculate(self):
        result = eval(self.leftSideValue + self.waitingOperator + self.rightSideValue);
        print(result);

        self.leftSideValue = str(result);
        self.rightSideValue = "";
        self.waitingOperator = "";

    def ClearData(self):
        self.currentInputStr = "";

