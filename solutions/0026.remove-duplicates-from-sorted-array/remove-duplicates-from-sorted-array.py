#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from __future__ import annotations

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        far = 1
        n = len(nums)
        while far < n:
            # print('cur:{}, far:{}'.format(cur,far))
            if nums[far] != nums[cur]:
                # 交换位置
                nums[cur+1], nums[far] = nums[far], nums[cur+1]
                cur += 1
            far += 1
        while cur < n:
            if cur+1 < n and nums[cur] < nums[cur+1]:
                cur +=1
            else:
                break
        # print(nums)
        # print(cur)
        return cur+1

    tests = [
        ([1], 1),
        ([1, 1, 2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),

    ]
# @lc code=end

