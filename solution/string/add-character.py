class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum = 0
        for i in t:
            sum += ord(i)
        for j in s:
            sum -= ord(j)
        return chr(sum)

s = Solution()
res = s.findTheDifference('adsssd', 'adsssdf')

print(res)