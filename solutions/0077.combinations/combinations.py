#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1: return []
        if n == 1: return [[1]]
        nums = [x for x in range(1, n+1)]
        i = 0
        ret = []
        def dfs(i, path):
            if len(path) == k:
                ret.append(path)
                return
            else:
                while i < n:
                    dfs(i+1, path + [nums[i]])
                    i += 1
        dfs(i, [])
        return ret

# @lc code=end

