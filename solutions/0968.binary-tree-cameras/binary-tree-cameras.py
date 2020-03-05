#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 1 -> 覆盖且没有相机
    # 2 -> 有相机
    # 0 -> 未覆盖
    def minCameraCover(self, root: TreeNode) -> int:
        ret = 0
        def dfs(node):
            nonlocal ret
            if not node: return 1
            l = dfs(node.left)
            r = dfs(node.right)
            # 首先看两个子节点是否有没有覆盖的 这种情况下把相机安装在父节点
            if l == 0 or r == 0:
                ret += 1
                return 2
            # 任一子节点安装了相机 则本节点已覆盖
            elif l == 2 or r == 2:
                return 1
            else:
                return 0
        # 如果根节点未被覆盖 则单独再安装一个相机
        if dfs(root) == 0:
            ret += 1
        return ret
# @lc code=end

