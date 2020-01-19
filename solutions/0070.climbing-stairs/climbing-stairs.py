#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划法
        # 时间复杂度: O(N)
        # 空间复杂度: O(1)

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        i = 3
        pre = 1
        cur = 2
        r = 0
        while i <= n:
            r = pre + cur
            pre = cur
            cur = r
            i += 1
        return r

    tests = [
        (2, 2),
        (3, 3),
    ]
# @lc code=end
