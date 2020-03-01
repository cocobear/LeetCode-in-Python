#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        ret = []
        if root:
            ret.append(root.val)
            ret.extend(self.preorderTraversal(root.left))
            ret.extend(self.preorderTraversal(root.right))
        return ret

    # 迭代法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                # 使用了stack 先进后出 所以先入right
                stack.append(node.right)
                stack.append(node.left)
        return ret
        
# @lc code=end

