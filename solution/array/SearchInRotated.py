class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        lo, hi = 0, len(nums) - 1
        min = self.findMinIndex(nums)
        print(min)
        maxValue = nums[min - 1]
        print(maxValue)
        if target < nums[min] or target > maxValue:
            return -1
        if target == nums[min]:
            return min
        if target <= nums[hi]:
            rlt = self.binarySearch(nums[min:hi + 1], target)
            return -1 if rlt == -1 else min + rlt
        if target >= nums[hi]:
            return self.binarySearch(nums[lo:min], target)

    def findMinIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1,
        while lo < hi:
            if nums[lo] < nums[hi]:
                return lo
            mid = (lo + hi) // 2
            # print(lo, mid, hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
                # print(lo, mid, hi)
        return lo

    def binarySearch(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    res = s.search([3, 1], 2)
    print(res)
    print(s.binarySearch([3], 3))
