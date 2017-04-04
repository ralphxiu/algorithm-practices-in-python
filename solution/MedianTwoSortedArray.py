class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # initialize the length and index variables
        l1, l2 = len(nums1), len(nums2)
        l = l1 + l2
        start1, end1, mid1, mid2 = 0, l1 - 1, 0, 0
        print(l, l1, l2, start1, end1, mid1, mid2, abs(l - 2 - 2 * (mid1 + mid2)) <= 1)
        # binary search
        while start1 <= end1 and abs(l - 2 * (mid1 + mid2 + 1)) > 1:
            mid1 = (start1 + end1) // 2
            mid2 = self.binarySearch(nums2, nums1[mid1])
            print(mid1, mid2)
            """
            right side weights more than left side
            i.e. the number that we picked is smaller than median
            """
            if l - 2 - 2 * (mid1 + mid2) > 0:
                start1 = mid1 + 1
            else:
                end1 = mid1 - 1

        print('mid1 is', mid1, 'mid2 is', mid2, nums1[mid1], nums2[mid2])
        if nums1[mid1] == nums2[mid2]:
            return nums1[mid1]
        if l - 2 - 2 * (mid1 + mid2) == 0:
            return nums1[mid1]
        elif l2 - 2 - 2* (mid1 + mid2) == 1: # right has one more number than left

    def binarySearch(self, nums, k):
        start, end = 0, len(nums) - 1
        print('starting')
        while start <= end:
            mid = (start + end) // 2
            print(start, mid, end)
            if nums[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        print(nums[start], nums[mid], nums[end])
        print(mid, nums[mid], k)
        if nums[mid] > k:
            mid -= 1
        print(mid, nums[mid], k)
        return mid


if __name__ == "__main__":
    s = Solution()
    # s.binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4.5)
    median = s.findMedianSortedArrays([1, 2, 3, 4, 5], [4, 7, 8, 9])
    # print(median)