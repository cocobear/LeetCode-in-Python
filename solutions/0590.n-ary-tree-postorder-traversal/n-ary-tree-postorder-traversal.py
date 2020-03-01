#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root: return []
        for child in root.children:
            ret.extend(self.postorder(child))
        ret.extend([root.val])

        return ret
# @lc code=end

