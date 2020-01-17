#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from __future__ import annotations

# @lc code=start
class Solution:
    def maxSubArrayBFO3(self, nums: List[int]) -> int:
        # 暴力法
        # 时间复杂度: O(N^3)
        # 空间复杂度: O(1)
        # 虽然只有两个for循环，但是里面计算和的时候使用了sum,所以又是一次循环
        max_sum = -2**31
        head = 0
        n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            for j in range(i, n):
                max_sum = max(max_sum, sum(nums[i:j+1]))
        return max_sum

    def maxSubArrayBFO2(self, nums: List[int]) -> int:
        # 暴力法
        # 时间复杂度: O(N^2)
        # 空间复杂度: O(1)
        # 因为求和放在了第二个循环中
        # 提交无法通过, 会超时
        max_sum = -2**31
        sums = 0
        head = 0
        n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            sums = 0
            for j in range(i, n):
                sums += nums[j]
                max_sum = max(max_sum, sums)
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划法
        # 时间复杂度: O(N)
        # 空间复杂度: O(1)
        n = len(nums)
        if n == 0:
            return 0
        res = nums[0]
        cur = res

        for i in range(1, n):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            res = max(res, cur)
        return res


    tests = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([], 0),
        ([-2, 1], 1),
        ([1, -2], 1),
        ([-2, -1], -1),
        ([1,2,-1,-2,2,1,-2,1,4,-5,4], 6),
        ([31,-41,59,26,-53,58,97,-93,-23,84], 187),
        ([-2, -3 , -1], -1),
    ]

# @lc code=end
