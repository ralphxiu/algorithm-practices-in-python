class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1,
        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = (lo + hi) / 2
            print(lo, mid, hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
            print(lo, mid, hi)
        print(lo, mid)
        return lo

if __name__ == "__main__":
    s = Solution()
    res = s.findMin([7, 8, 1, 3, 4, 5, 6])
    print(res)