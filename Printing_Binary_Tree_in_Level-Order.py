# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return res
        tmp = [root]
        while tmp:
            node = tmp.pop(0)
            res.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        return res


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(6)

    s = Solution()
    print s.PrintFromTopToBottom(tree)
