#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归DFS方式
        if not p or not q:
            return p == q
        if p.val != q.val: return False
        a = self.isSameTree(p.left, q.left)
        b = self.isSameTree(p.right, q.right)
        return a and b


# @lc code=end
