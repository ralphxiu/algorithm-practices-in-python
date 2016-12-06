class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in nums:
            if len(arr) < 3:
                if i not in arr:
                    arr.append(i)
                    arr.sort(reverse=True)
                print(arr)
            else:
                for j in range(len(arr)):
                    if i == arr[j]:
                        print('break')
                        break
                    if i > arr[j]:
                        arr[j] = i
                    print(i, arr[j], arr)
        return arr[2] if len(arr) == 3 else arr[0]

if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([4, 3, 2, 6]))