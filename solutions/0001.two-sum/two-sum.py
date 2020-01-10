#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity : O(n^2)
        # Space complexity : O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i,j]
    tests = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 7, 0, 1], 3, [0, 2]),

            ]

# @lc code=end
