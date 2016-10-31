class AddMultiply:
    def makeExpression(self, y):
        x1 = 1
        x2 = y
        x3 = 0
        return self.equationHelper(x1, x2, x3, y)

    def equationHelper(self, x1, x2, x3, y):
        if x1 == 0 or x1 == 1:
            return self.equationHelper(x1 + 1, x2, x3 - x2, y)
        elif x2 == 0 or x2 == 1:
            return self.equationHelper(x1, x2 + 1, x3 - x1, y)
        elif x3 == 0 or x3 == 1:
            return self.equationHelper(x1, x2 + 1, x3 - x1, y)
        else:
            return (x1, x2, x3)

addm = AddMultiply()

print(addm.makeExpression(11))