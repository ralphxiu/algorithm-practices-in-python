"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).
"""


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        sumA = sum(A)
        ftemp = sum((i * A[i]) for i in range(n))
        maxA = ftemp
        print(ftemp)
        for j in range(1, n):
            ftemp = ftemp + sumA - n * A[-j]
            if ftemp > maxA:
                maxA = ftemp
            print(ftemp)
        return maxA

if __name__ == "__main__":
    s = Solution()
    print(s.maxRotateFunction([4, 3, 2, 6]))
    #print(s.maxRotateFunction())
    #print(s.maxRotateFunction())
