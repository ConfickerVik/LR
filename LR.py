
class LR:
    def __init__(self):
        self.curState = ""
        self.curToken = ""
        self.stack_state = []
        self.stack_state.append(0)
        self.stack_char = []
        self.chain = "(n+n)+n$"
        self.index = 0
        self.a = ''

    def main(self):
        while True:
            self.a = self.chain[self.index]
            self.getActionType()
            self.a = self.chain[self.index]
            if self.stack_char[-1] == "E" and self.stack_state[-1] == 1:
                return "Цепочка распознана!"

    def getActionType(self):

        if self.a == "n":
            state = self.stack_state[-1]
            if state == 0:
                self.stack_state.append(3)
                self.stack_char.append(self.a)
                self.index += 1
            elif state == 4:
                self.stack_state.append(3)
                self.stack_char.append(self.a)
                self.index += 1
            elif state == 5:
                self.stack_state.append(3)
                self.stack_char.append(self.a)
                self.index += 1

        elif self.a == "+":
            return self.actionForPlus()
        elif self.a == "(":
            state = self.stack_state[-1]
            if state == 0:
                self.stack_state.append(4)
                self.stack_char.append(self.a)
                self.index += 1
            elif state == 4:
                self.stack_state.append(4)
                self.stack_char.append(self.a)
                self.index += 1
            elif state == 5:
                self.stack_state.append(4)
                self.stack_char.append(self.a)
                self.index += 1
        elif self.a == ")":
            state = self.stack_state[-1]
            if state == 2:
                self.R2()
                self.GoTo()
            elif state == 3:
                self.R3()
                self.GoTo()
            elif state == 6:
                self.stack_state.append(8)
                self.stack_char.append(self.a)
                self.index += 1
            elif state == 7:
                self.R1()
                self.GoTo()
            elif state == 8:
                self.R4()
                self.GoTo()

        elif self.a == "$":
            state = self.stack_state[-1]
            if state == 2:
                self.R2()
                self.GoTo()
            elif state == 3:
                self.R3()
                self.GoTo()
            elif state == 7:
                self.R1()
                self.GoTo()
            elif state == 8:
                self.R4()
                self.GoTo()

    def actionForPlus(self):
        state = self.stack_state[-1]
        if state == 1:
            self.stack_state.append(5)
            self.stack_char.append(self.a)
            self.index += 1
        elif state == 2:
            self.R2()
            self.GoTo()
        elif state == 3:
            self.R3()
            self.GoTo()
        elif state == 6:
            self.stack_state.append(5)
            self.stack_char.append(self.a)
            self.index += 1
        elif state == 7:
            self.R1()
            self.GoTo()
        elif state == 8:
            self.R4()
            self.GoTo()

    def R1(self):
        for i in range(3):
            self.stack_state.pop(-1)
            self.stack_char.pop(-1)
        self.stack_char.append("E")

    def R2(self):
        self.stack_state.pop(-1)
        self.stack_char.pop(-1)
        self.stack_char.append("E")

    def R3(self):
        self.stack_state.pop(-1)
        self.stack_char.pop(-1)
        self.stack_char.append("T")

    def R4(self):
        for i in range(3):
            self.stack_state.pop(-1)
            self.stack_char.pop(-1)
        self.stack_char.append("T")

    def GoTo(self):
        symbol = self.stack_char[-1]
        if symbol == "E":
            state = self.stack_state[-1]
            if state == 0:
                self.stack_state.append(1)
            elif state == 4:
                self.stack_state.append(6)
        elif symbol == "T":
            state = self.stack_state[-1]
            if state == 0:
                self.stack_state.append(2)
            elif state == 4:
                self.stack_state.append(2)
            elif state == 5:
                self.stack_state.append(7)


if __name__ == '__main__':
    print(LR().main())
