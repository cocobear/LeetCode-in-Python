#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from __future__ import annotations

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        i, j = 0, n - 1
        while i < j:
            max_area = max(max_area, min(height[i],height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([2,3,4,5,18,17,6], 17),
    ]
# @lc code=end

