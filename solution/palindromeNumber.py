class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        halfLen = len(x) // 2
        for i in range(halfLen):
            if x[i] != x[-1-i]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(-10))
    print(s.isPalindrome(12321))
    print(s.isPalindrome(14699641))