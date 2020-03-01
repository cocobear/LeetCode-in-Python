#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
# @lc code=end

