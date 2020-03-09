#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ret = float('inf')
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
                if abs(target - ret) > abs(target - s):
                    ret = s
        return ret
# @lc code=end

