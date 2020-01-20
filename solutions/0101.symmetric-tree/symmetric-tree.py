#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from LeetCode_in_Python.datastruct.ListNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归法

        if not root: return True
        def isSym(left, right):
            if left and right:
                if left.val != right.val: return False
                a = isSym(left.left, right.right)
                b = isSym(left.right, right.left)
                return a and b
            elif left or right:
                return False
            else:
                return True
        return isSym(root.left, root.right)

# @lc code=end
