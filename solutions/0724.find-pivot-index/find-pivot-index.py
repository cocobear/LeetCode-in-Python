#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from __future__ import annotations
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        half = 0
        for i in range(len(nums)):
            if (total - nums[i]) / 2 == half:
                return i
            half += nums[i]
           
        return -1
    tests = [
        ([1,7,3,6,5,6], 3),
    ]
        
# @lc code=end

