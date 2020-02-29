#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        candidates.sort()
        ret = []
        i = 0
        def dfs(i, path):
            if sum(path) == target:
                ret.append(path)
                return
            elif sum(path) < target:
                while i < len(candidates):
                    dfs(i, path + [candidates[i]])
                    i += 1
        dfs(i, [])

        return ret
# @lc code=end

