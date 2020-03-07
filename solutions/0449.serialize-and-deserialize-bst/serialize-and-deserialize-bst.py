#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ret = []
        def helper(node):
            if node == None: return ''
            ret.append( str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return ','.join(ret)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        def helper(data):
            if data == []: return
            cur = int(data.pop(0))
            root = TreeNode(cur)
            root.left = helper([x for x in data if int(x) < cur ])
            root.right = helper([x for x in data if int(x) > cur])

            return root

        data = data.split(',')
        return helper(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

