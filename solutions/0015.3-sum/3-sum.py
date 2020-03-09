#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        n = len(nums) - 1
        for i in range(n-1):
            # 去掉重复的数字
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i + 1
            k = n
            while j < k:
                s = nums[k] + nums[j]
                if s == target:
                    ret.append([nums[i],nums[j],nums[k]])
                    # 去掉重复的数字
                    while j+1 < n and nums[j] == nums[j+1]:
                        j += 1
                    while k-1 > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return ret


# @lc code=end

