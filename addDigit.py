class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9

    def addDigitsBrute(self, num):
        sum = 0
        len = num // 10
        if len == 0:
            return sum
        else:
            for i in range(len):
                sum += num // 10 ^ i - num // 10 ^ (i - 1)
            if num // 10 > 0:
                return self.addDigitsBrute(num)
            else:
                return num

s = Solution()
print(s.addDigits(1999), s.addDigitsBrute(1999))