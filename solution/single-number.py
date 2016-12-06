class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        sorted_nums = sorted(nums)
        for idx, el in enumerate(sorted_nums):
            if idx == 0 and el != sorted_nums[1]:
                return el
            if idx == len(sorted_nums) - 1 and el != sorted_nums[idx - 1]:
                return el
            if el != sorted_nums[idx - 1] and el != sorted_nums[idx + 1]:
                return el
        return None

s = Solution()
result = s.singleNumber([-1, -2, -3, 4, 5, -3, -1, -2, 5])
print(result)