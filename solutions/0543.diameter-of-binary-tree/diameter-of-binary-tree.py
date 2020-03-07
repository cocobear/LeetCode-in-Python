#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)

            longest = left + right
            self.ret = max(self.ret, longest)
            return max(left, right) + 1
        self.ret = 0
        helper(root)
        return self.ret

# @lc code=end

