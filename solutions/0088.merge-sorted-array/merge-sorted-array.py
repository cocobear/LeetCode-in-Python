#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from __future__ import annotations

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        i = 0
        j = m + n - 1
        while n >=1 or m >= 1:
            if n == 0:
                nums1[j] = nums1[m-1]
                m -= 1
            elif m == 0 or nums1[m-1] < nums2[n-1]:
                nums1[j] = nums2[n-1]
                n -= 1
            else:
                nums1[j] = nums1[m-1]
                m -= 1
            j -= 1
        return nums1

    tests = [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6]),
    ]
# @lc code=end

if __name__ == "__main__":
    m = [1,2,3,0,0,0]
    Solution().merge(m, 3, [2,5,6], 3)
    print(m)