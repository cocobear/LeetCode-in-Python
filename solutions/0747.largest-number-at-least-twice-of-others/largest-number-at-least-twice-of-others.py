#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
from __future__ import annotations
# @lc code=start
class Solution:       
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0 
        max_num = max(nums)
        max_index = nums.index(max_num)
        del nums[max_index]
        if max_num >= max(nums)*2:
            return max_index
        else:
            return -1
    tests = [
        ([0,0,1,2], 3),
        ([1], 0),
        ([1, 2, 3, 4], -1),
        ([1,0], 0)
    ]
# @lc code=end

