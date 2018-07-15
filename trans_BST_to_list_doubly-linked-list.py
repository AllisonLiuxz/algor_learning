# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        def find_head(root):
            if not root:
                return None
            if not root.left:
                return root
            return find_head(root.left)

        def link_tree(root, pre):
            if not root:
                return None
            if not root.left and not root.right:
                if pre:
                    root.left = pre
                    pre.right = root
                root.right = None
                return root
            if root.left:
                cur_pre = link_tree(root.left, pre)
                root.left = cur_pre
                cur_pre.right = root
            else:
                if pre:
                    root.left = pre
                    pre.right = root
            if root.right:
                cur_next = link_tree(root.right, root)
            else:
                cur_next = root
            cur_next.right = None
            return cur_next
        head = find_head(pRootOfTree)
        link_tree(pRootOfTree, None)
        return head

if __name__ == '__main__':
    s = Solution()
    t0 = TreeNode(5)
    t1 = TreeNode(3)
    t2 = TreeNode(8)
    t3 = TreeNode(2)
    t4 = TreeNode(4)
    t5 = TreeNode(7)
    t6 = TreeNode(9)
    t0.left = t1
    t0.right = t2
    t1.left = t3
    t1.right = t4
    t2.left = t5
    t2.right = t6

    head = s.Convert(t0)
    cur = head
    while cur:
        print cur.val
        tmp = cur
        cur = cur.right
    tail = tmp
    cur = tail
    print "Reverse:"
    while cur:
        print cur.val
        cur = cur.left

