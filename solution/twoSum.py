class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i

if __name__ == "__main__":
    s = Solution()
    res = s.twoSum([4, 6, 3, 2, 9], 9)
    print(res)