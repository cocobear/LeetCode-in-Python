#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from __future__ import annotations
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return None
        if n == 1: return ['()']
        ret = []
        l, r = n, n
        def dfs(l, r, path):
            if l == 0 and r == 0:
                ret.append(path[:])
                return
            if r < l or l == -1 or r == -1:
                return
            else:
                dfs(l-1, r, path+'(')
                dfs(l, r-1, path+')')

        dfs(r, l, '')

        return ret
    tests = [
        (3, [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
            ]),
    ]
# @lc code=end

