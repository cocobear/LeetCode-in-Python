#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.count = 0
        self.dfs(root, target)
        return self.count
        
    def dfs(self, node, target):
        if not node: return
        self.testNode(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        

    def testNode(self, node, target):
        if not node: return
        if node.val == target:
            self.count += 1
        self.testNode(node.left, target-node.val)
        self.testNode(node.right, target-node.val)

        
# @lc code=end

