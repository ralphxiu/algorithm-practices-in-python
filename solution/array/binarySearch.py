class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid + 1
            if A[mid] > target:
                end = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    res = s.findPosition([1, 2, 2, 3, 5, 5, 6], 5)
    print(res)