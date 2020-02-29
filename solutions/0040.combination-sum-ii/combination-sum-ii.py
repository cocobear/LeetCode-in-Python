#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        # 使用set数据结构， 避免重复的组合
        ret = set()
        i = 0
        candidates.sort()
        def dfs(i, path):
            if sum(path) == target:
                # 将list转换为tuple 才可以用在set里
                ret.add(tuple(path))
                return
            elif sum(path) < target:
                while i < len(candidates):
                    dfs(i+1, path + [candidates[i]])
                    i += 1
        dfs(i, [])

        return [list(a) for a in ret]
# @lc code=end

