class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        elif n == 2 * (n >> 1) + 1:
            return 1 + self.hammingWeight(n >> 1)
        elif n == 2 * (n >> 1):
            return 0 + self.hammingWeight(n >> 1)


sol = Solution()
print(sol.hammingWeight(1551234212))
