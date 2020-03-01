#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        array = []
        def dfs(node, x, y):
            if node:
                array.append((x,y,node.val))
                dfs(node.left, x-1, y-1)
                dfs(node.right, x+1, y-1)
        dfs(root, 0, 0)
        print(array)
        dd = sorted(array, key=lambda x: (x[0], -x[1], x[2])) # python 排序函数可以很方便的一次写多个条件～
        print(dd)
        pre = dd[0][0]
        tmp = []
        ret = []
        for item in dd:
            if pre == item[0]:
                tmp.append(item[2])
            else:
                if tmp:
                    ret.append(tmp)
                tmp = []
                tmp.append(item[2])
                pre = item[0]

        if tmp:
            ret.append(tmp)
        return ret
            

    tests = [
        (1,2)
    ]

        
# @lc code=end

