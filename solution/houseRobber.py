class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, i = [0]*2, 1
        while i <= len(nums):
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i - 1])
            i += 1
        return dp[(i - 1) % 2]

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2]))
