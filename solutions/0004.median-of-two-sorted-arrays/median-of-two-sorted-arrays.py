#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from __future__ import annotations

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        new_list = []
        i = 0
        j = 0
        while i < m or j < n:
            # print('i={}, j={}, new_list= {}'.format(i,j, new_list))
            if i >= m:
                new_list.extend(nums2[j:])
                break
            if j >= n:
                new_list.extend(nums1[i:])
                break
            else:
                if nums1[i] <= nums2[j]:
                    new_list.append(nums1[i])
                    i += 1
                else:
                    new_list.append(nums2[j])
                    j += 1
        #new_list = list(set(nums1 + nums2))
        new_list.sort()

        x = len(new_list)
        # print(new_list)
        if x %2 == 0:
            return (new_list[x//2]+new_list[x//2-1])/2.0
        else:
            return float(new_list[x//2])
    tests = [
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([1,1], [1,2], 1.0)

            ]
# @lc code=end

