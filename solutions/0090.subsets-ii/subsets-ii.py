#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

from __future__ import annotations
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        ret = set()
        def dfs(i, path):
            path.sort()
            ret.add(tuple(path))
            while i < len(nums):
                dfs(i+1, path+[nums[i]])
                i += 1
        dfs(0, [])

        a = [list(x) for x in ret]
        a.sort()
        print(a)
        return a

    tests = [
        ([4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]),
    ]
        
# @lc code=end

