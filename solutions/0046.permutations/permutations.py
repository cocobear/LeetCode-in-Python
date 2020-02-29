#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from __future__ import annotations
# @lc code=start
class Solution:
    # DFS方法
    def permuteDFS(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        n = len(nums)
        ret = []
        def dfs(nums, path):
            if not nums:
                ret.append(path)
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs(nums, [])

        return ret

    # backtrack方法
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        ret = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                ret.append(track[:])
                return
            for num in nums:
                if num in track:
                    continue
                track.append(num)
                backtrack(nums, track)
                track.pop()
        backtrack(nums, [])
        return ret

    tests = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ]
# @lc code=end

