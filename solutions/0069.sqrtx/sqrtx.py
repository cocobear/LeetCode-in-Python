#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        j = x
        r = 1
        if x <= 1:
            return x
        while i < j:
            if j*j == x:
                return j
            elif i*i == x:
                return i
            if j - i == 1:
                break
            tmp =  (j + i) // 2
            if tmp*tmp > x:
                j = tmp
            elif tmp*tmp < x:
                i = tmp
            else:
                return tmp

        return i

    tests = [
        (5, 2),
        (2, 1),
        (4, 2),
        (8, 2),
        (16, 4),
        (0, 0),
        (36, 6),
    ]
# @lc code=end
