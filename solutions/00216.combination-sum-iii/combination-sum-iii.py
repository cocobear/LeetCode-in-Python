#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from __future__ import annotations
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n: return None
        if n == 1: return [[1]]
        ret = []
        nums = [x for x in range(1, n+1)]
        def dfs(i, path):
            if len(path) > k:
                return
            if i > 9:
                return
            if sum(path) == n and len(path) == k:
                ret.append(path)
            if sum(path) < n:
                while i < n:
                    dfs(i+1, path + [nums[i]])
                    i += 1
        dfs(0, [])
        ret.sort()
        return ret
    
    tests = [
        (3, 7, [[1,2,4]]),
        (2, 18, []),
        (3, 15, [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]])
    ]

# @lc code=end

