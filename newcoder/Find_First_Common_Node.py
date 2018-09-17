# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1.next else pHead2
            cur2 = cur2.next if cur2.next else pHead1
        return cur1


if __name__ == '__main__':
    s = Solution()
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h6 = ListNode(6)
    h7 = ListNode(7)
    h8 = ListNode(8)
    h9 = ListNode(9)

    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = h6
    h6.next = h7
    h7.next = h8
    h8.next = h9

    p1 = ListNode(10)
    p2 = ListNode(11)
    p3 = ListNode(12)
    p4 = ListNode(13)
    p5 = ListNode(14)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    p5.next = h9

    out = s.FindFirstCommonNode(h1, p1)
    print out.val
