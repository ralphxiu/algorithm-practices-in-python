class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        n = len(costs)
        for i in range(1, n):
            for j in range(3):
                costs[i][j] = min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3]) + costs[i][j]
        return min(costs[n - 1])

if __name__ == "__main__":
    s = Solution()
    print(s.minCost([[14,2,11],[11,14,5],[14,3,10]]))()