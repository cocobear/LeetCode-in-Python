#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

from __future__ import annotations
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        ret = set()
        def dfs(nums, path):
            if not nums:
                ret.add(tuple(path))
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])

        dfs(nums, [])
        print(ret)
        return [list(x) for x in ret]

    tests = [
        ([1,1,2], [[1, 2, 1], [2, 1, 1], [1, 1, 2]]),
    ]

# @lc code=end

