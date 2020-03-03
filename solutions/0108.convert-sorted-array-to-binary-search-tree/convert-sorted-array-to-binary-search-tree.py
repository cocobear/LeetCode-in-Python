#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
from __future__ import annotations
from LeetCode_in_Python.datastruct.TreeNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST_O2(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if not n:
            return
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return
        n = len(nums) - 1
        def helper(root, start, end):
            if start == end:
                return TreeNode(nums[start])
            elif start < end:
                mid = (start + end) // 2
                root = TreeNode(nums[mid])
                root.left = helper(root, start, mid-1)
                root.right = helper(root, mid+1, end)
                return root
        root = None
        return helper(root, 0, n)

# @lc code=end

    tests = [
        ([-10,-3,0,5,9], TreeNode.constructTree([0 ,-3, 5, -10 ,None, None, 9]))
    ]