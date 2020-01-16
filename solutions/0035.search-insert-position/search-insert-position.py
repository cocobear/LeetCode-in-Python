#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from __future__ import annotations

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cur = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i += 1
            else:
                return i
            
        return i
    tests = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
    ]
# @lc code=end
