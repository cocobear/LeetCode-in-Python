#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
from __future__ import annotations
# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        pass
        nums.sort()
        ans = [nums[i] for i in range(0, len(nums), 2)]
        # print(ans)
        return sum(ans)
    tests = [
        ([1,4,3,2], 4),
    ]
        
# @lc code=end

