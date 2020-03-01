#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(a, b):
            if a == None and b == None:
                return True
            elif a and not b or b and not a:
                return False
            if a.val != b.val: return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)

        def dfs(node):
            if not node: return False
            if node.val == t.val and isSame(node, t):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(s)

        
# @lc code=end

