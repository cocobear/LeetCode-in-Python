#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

from __future__ import annotations
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res

    tests = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4)
    ]
        
# @lc code=end

