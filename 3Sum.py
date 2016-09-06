class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rslt = []
        plus = sorted(list(filter(lambda x: x >= 0, nums)))
        minus = list(filter(lambda x: x < 0, nums))
        minus.sort(reverse=True)
        i, j = 0, 0
        while i < len(plus) and j < len(minus):
            partialSum = plus[i] + minus[j]
            if partialSum > 0:
                if -partialSum in minus:
                    rslt.append([plus[i], minus[j], -partialSum])
                else:
                    i += 1
            else:
                if -partialSum in plus:
                    rslt.append([plus[i], -partialSum, minus[j]])
                else:
                    j += 1
        return rslt

if __name__ == "__main__":
    s = Solution()
    res = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(res)