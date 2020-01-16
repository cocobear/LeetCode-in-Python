#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from __future__ import annotations

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        cur = 0
        far = 1

        while cur < n:
            far = cur + 1
            # print('cur:{}, far:{}, nums:{}'.format(cur,far,nums))

            if nums[cur] == val:
                while far < n:
                    if nums[far] != val:
                        nums[cur], nums[far] = nums[far], nums[cur]
                        break
                    far += 1
            cur += 1
        cur = 0
        while cur < n:
            if nums[cur] == val:
                break
            cur += 1
        return cur

    tests = [
        ([0,1,2,2,3,0,4,2], 2, 5),
        ([3,2,2,3], 3, 2),
    ]
# @lc code=end

