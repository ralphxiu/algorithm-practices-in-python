class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def removeDuplicatesHelper(nums, idx):
            while idx < len(nums):
                nums[idx - 1] = nums[idx]
                idx += 1
            nums[idx - 1] = None

        proceeding, following = 0, 1
        while proceeding < len(nums) - 1:
            if nums[proceeding] == nums[following]:
                removeDuplicatesHelper(nums, proceeding + 1)
            else:
                proceeding += 1
                following += 1
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = s.removeDuplicates([1, 1, 1, 2, 2, 2])
    print(nums)