class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, depth=0):
        ret = ''
        if self.right != None:
            ret += self.right.__str__(depth + 1)
        if not self.val:
            ret += '\n'
        else:
            ret += '\n' + ('    '*depth) + str(self.val)
        if self.left != None:
            ret += self.left.__str__(depth + 1)
        return ret

    @staticmethod
    def constructTree(levelOrder):
        # 从给定的层先遍历的数组构建一个二叉树
        # 给定的数组为一个满二叉树
        def conTree(root, levelOrder, i):
            if i >= len(levelOrder):
                return
            if not levelOrder[i]:
                return
            tmp = TreeNode(levelOrder[i])
            root = tmp
            root.left = conTree(root.left, levelOrder, 2*i+1)
            root.right = conTree(root.right, levelOrder, 2*i+2)
            return root

        root = None
        return conTree(root, levelOrder, 0)


if __name__ == "__main__":
    print(TreeNode.constructTree([3,9,20,None,None,15,7]))
    print(TreeNode.constructTree([2,3,4]))
