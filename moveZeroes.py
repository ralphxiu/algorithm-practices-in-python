class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0 #points to the first non-zero
        z = 0 #points
        while n < len(nums):
            if nums[n] == 0:
                n += 1
                continue
            if nums[z] != 0:
                z += 1
                continue
            nums[z] = nums[n]
            nums[n] = 0
            z += 1
            n += 1

        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([1, 0, 1]))
