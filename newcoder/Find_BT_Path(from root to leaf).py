# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root or expectNumber is None:
            return []
        res = []

        def helper(root, number, path):
            print path
            if not root:
                return None
            path.append(root.val)
            if not root.left and not root.right and root.val == number:
                    res.append(path[:])
            helper(root.left, number-root.val, path)
            helper(root.right, number - root.val, path)
            path.pop()

        helper(root, expectNumber, [])
        print res
if __name__ == '__main__':
    s = Solution()
    t0 = TreeNode(12)
    t1 = TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(2)
    t4 = TreeNode(9)
    t5 = TreeNode(6)
    t6 = TreeNode(4)
    t0.left = t1
    t0.right = t2
    t1.left = t3
    t1.right = t4
    t2.left = t5
    t2.right = t6
    # t.left = t
    # t.right = t

    s.FindPath(t0, 0)