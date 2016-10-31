class ABBADiv1:
    def canObtain(self, initial, target):
        if self.canObtainBool(initial, target):
            return "Possible"
        else:
            return "Impossible"

    def canObtainBool(self, initial, target):
        if len(initial) == len(target):
            if initial == target:
                return True
            else:
                return False
        elif len(target) == 1:
            return False
        if (target[0], target[-1]) == ('B', 'B'):
            return self.canObtainBool(initial, self.reverseRule2(target))
        elif (target[0], target[-1]) == ('B', 'A'):
            return self.canObtainBool(initial, self.reverseRule1(target)) or self.canObtainBool(initial, self.reverseRule2(target))
        elif (target[0], target[-1]) == ('A', 'A'):
            return self.canObtainBool(initial, self.reverseRule1(target))
        else:
            return False

    def reverseRule2(self, target):
        return target[1:][::-1]

    def reverseRule1(self, target):
        return target[:-1]


abba = ABBADiv1()

print(abba.reverseRule2('BABABA'))
#print(abba.canObtain('A', 'ABBA'))
#print(abba.canObtain('A', 'BABA'))
print(abba.canObtain('AAABAAABB', 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'))