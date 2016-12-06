class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        myDict = dict()
        tDict = dict()
        for i in range(len(s)):
            if s[i] in myDict:
                if myDict[s[i]] != t[i]:
                    return False
            elif tDict.get(t[i]):
                return False
            else:
                myDict[s[i]] = t[i]
                tDict[t[i]] = True
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic('foo', 'bar'))
    print(s.isIsomorphic('fol', 'bar'))
    print(s.isIsomorphic('ab', 'aa'))