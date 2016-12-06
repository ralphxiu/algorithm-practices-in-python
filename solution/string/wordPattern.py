class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        arr = str.split(" ")
        hashTable = {}
        revHashTable = {}
        if len(pattern) != len(arr):
            return False
        for i in range(len(pattern)):
            if hashTable.get(pattern[i]):
                if hashTable[pattern[i]] != arr[i]:
                    return False
            elif revHashTable.get(arr[i]):
                return False
            else:
                hashTable[pattern[i]] = arr[i]
                revHashTable[arr[i]] = True
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern('aba', 'too far too'))
    print(s.wordPattern('fol', 'a a c'))
    print(s.wordPattern('ab', 'aa ab'))