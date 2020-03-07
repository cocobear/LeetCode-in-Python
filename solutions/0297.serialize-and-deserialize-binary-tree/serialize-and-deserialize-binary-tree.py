#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []

        def helper(node):
            if node == None:
                ret.append('*')
                return
            else:
                ret.append(str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return ','.join(ret)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def helper(data):
            val = data.pop(0)
            if val == '*':
                return None
            root = TreeNode(int(val))
            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

