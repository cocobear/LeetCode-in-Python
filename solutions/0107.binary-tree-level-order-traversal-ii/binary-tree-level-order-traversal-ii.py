#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 递归法
        # 时间复杂度: O(N^2)
        # 空间复杂度: O(N)
        res = []
        def dfs(root: TreeNode, level: int, res: List[List[int]]):
            if root:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(root.val)
                dfs(root.left, level+1, res)
                dfs(root.right, level+1, res)
        dfs(root, 0, res)
        return res

# @lc code=end

    tests = [
        (TreeNode.constructTree([3,9,20,None,None,15,7]), [
                                    [15,7],
                                    [9,20],
                                    [3]
                                  ]
        ),
    ]