class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        start, end = 0, len(nums) -1
        while start < end:
            mid = (start + end + 1) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid - 1
            print(start, end)
        return start if nums[start] == target else -1

if __name__ == "__main__":
    s = Solution()
    print(s.binarySearch([1, 4, 4, 5, 5, 7, 7, 7, 7, 8, 8, 9], 4))