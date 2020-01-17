
from __future__ import annotations

import functools

class Solution:
    @functools.lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        # 递归法
        # 时间复杂度: O(2^N)
        # 空间复杂度: O(N)
        if n < 2:
            return n
        else:
            return (self.fib(n-1) + self.fib(n-2))

    def fib1(self, n:int) -> int:
        # 动态规划法
        # 时间复杂度: O(N)
        # 空间复杂度: O(1)
        if n < 2:
            return n
        cur = 1
        pre = 0
        res = 0
        for i in range(2, n+1):
            res = pre + cur
            pre = cur
            cur = res
        return res

    tests = [
        (3, 2),
        (4, 3),
        (50, 12586269025)
    ]

if __name__ == "__main__":
    for i in range(100):
        print(i, Solution().fib1(i))