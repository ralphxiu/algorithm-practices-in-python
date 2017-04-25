class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        return self.depthSumHelper(nestedList, 1)

    def depthSumHelper(self, list, depth):
        sum = 0
        for i in list:
            print(i)
            if type(i) is int:
                sum += i
            if type(i) is list:
                print('enter')
                sum += self.depthSumHelper(i, depth + 1)
        print(depth)
        return depth * sum

if __name__ == "__main__":
    s = Solution()
    print(s.depthSum([[1], 2, 3, [1, 1]]))