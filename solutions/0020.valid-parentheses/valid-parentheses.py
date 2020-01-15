#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        heap = []
        def get_oppo(s):
            if s == ')':
                return '('
            elif s == '}':
                return '{'
            elif s == ']':
                return '['

        for x in s:
            try:
                if x in ')}]':
                    tmp = heap.pop()
                    if tmp != get_oppo(x):
                        return False
                else:
                    heap.append(x)
            except IndexError:
                return False
        if heap:
            return False
        else:
            return True

    tests = [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
        ('[', False),
        (']', False)

    ]
# @lc code=end

