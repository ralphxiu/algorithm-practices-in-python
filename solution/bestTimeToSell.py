class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        difference = 0
        lowest = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            elif difference < i - lowest:
                difference = i - lowest

        return difference

s = Solution()
print(s.maxProfit([7, 2, 6, 1, 3, 4, 2]))
print(s.maxProfit([7, 1, 5, 9, 3, 6, 2]))