class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid:
            return 0
        # m is the number of rows, n is the number of cols
        m, n = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.bfs(grid, visited, i, j)
                    count += 1
                    print('bingo', count, i, j)
        return count

    def bfs(self, grid, visited, i, j):
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(i, j)]
        while len(queue):
            print(queue)
            newqueue = []
            for x, y in queue:
                visited[x][y] = True
                for dx, dy in deltas:
                    if self.check(grid, visited, x + dx, y + dy):
                        newqueue.append((x + dx, y + dy))
            queue = newqueue

    def check(self, grid, visited, i, j):
        m, n = len(grid), len(grid[0])
        return 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and not visited[i][j]

if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]))