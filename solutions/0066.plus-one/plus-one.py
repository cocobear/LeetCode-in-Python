#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from __future__ import annotations

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(a) for a in digits])
        n = int(s) + 1
        return [int(x) for x in str(n)]

    def plusOne(self, digits: List[int]) -> List[int]:
        one = [1]
        n = len(digits)
        i = n - 1
        extra = 1
        while i >= 0:
            x = digits[i] + extra
            extra = x // 10
            digits[i] = x % 10
            i -= 1

        # print(digits, extra)
        if extra:
            return [extra] + digits
        else:
            return digits

    tests = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([4,9], [5,0]),
        ([0], [1]),
        ([9,9], [1,0,0]),
    ]
# @lc code=end

