class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_str = ''
        max = 0
        for ch in s:
            if not ch in new_str:
                new_str += ch
            else:
                max = len(new_str) if len(new_str) > max else max
                idx = new_str.find(ch)
                new_str = new_str[idx+1:] + ch
        max = len(new_str) if len(new_str) > max else max
        return max

if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring('abcghdabcdabcde')
    print(res)