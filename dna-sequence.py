class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hash = {}
        arr = []
        for i in range(len(s) - 10 + 1):
            string = s[i:i+10]
            print(i, string)
            hash[string] = hash.get(string, 0) + 1
        print(hash)
        for key, val in hash.items():
            if val == 2:
                arr.append(key)
        return arr

s = Solution()
test = 'AAAAAAAAAAA'
res = s.findRepeatedDnaSequences(test)
print(res)