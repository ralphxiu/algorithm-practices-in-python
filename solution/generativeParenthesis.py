class Solution(object):
    def dfs(self, stack, n, str, ans, nl, nr):
        if n == 0 and stack == 0:
            ans.append(str)
        else:
            if nl > 0 and stack <= n and (n != 1 or stack != 1):
                ntr = str + '('
                self.dfs(stack + 1, n, ntr, ans, nl - 1, nr)
            if nr > 0 and stack > 0:
                ntr = str + ')'
                self.dfs(stack - 1, n - 1, ntr, ans, nl, nr - 1)

    def generateParenthesis(self, n):
        ans = []
        str = ""
        stack = 0
        self.dfs(stack, n, str, ans, n, n)

        return ans