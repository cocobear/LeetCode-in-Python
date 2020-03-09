#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        pre = j
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                pre = j
                j += 1
            elif pre != j and typed[pre] == typed[j]:
                pre = j
                j += 1

            else:
                return False
        if i == len(name):
            if j == len(typed):
                return True
            else:
                pass
                while j < len(typed):
                    if typed[j] != typed[pre]:
                        return False
                    j += 1
                return True
        else:
            return False
    tests = [
        ("vtkgn","vttkgnn", True)
    ]
# @lc code=end

