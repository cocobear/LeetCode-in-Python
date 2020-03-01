#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root:
            return []
        ret = [root.val]
        for child in root.children:
            ret.extend(self.preorder(child))
        return ret
        
# @lc code=end

