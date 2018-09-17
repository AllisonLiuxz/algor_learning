# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = tmp
            cur = tmp

        rHead = pHead.next
        cur = pHead
        while cur:
            new_cur = cur.next
            if cur.random:
                new_cur.random = cur.random.next
            cur = new_cur.next

        cur = pHead
        new_cur = rHead
        while new_cur.next:
            cur.next = new_cur.next
            new_cur.next = cur.next.next
            cur = cur.next
            new_cur = new_cur.next
        cur.next, new_cur.next = None, None
        return rHead

    # #####时间O(n),空间O(n)解法######
    # def Clone(self, pHead):
    #     # write code here
    #     if not pHead:
    #         return None
    #     node_map = {}
    #     rHead = RandomListNode(pHead.label)
    #     node_map[pHead] = rHead
    #     cur = pHead
    #     new_cur = rHead
    #     while cur.next:
    #         new_cur.next = RandomListNode(cur.next.label)
    #         cur = cur.next
    #         new_cur = new_cur.next
    #         node_map[cur] = new_cur
    #     node_map[None] = None
    #     cur = pHead
    #     new_cur = rHead
    #     while cur and new_cur:
    #         new_cur.random = node_map[cur.random]
    #         cur = cur.next
    #         new_cur = new_cur.next
    #     return rHead

if __name__ == '__main__':
    s = Solution()
    head = RandomListNode(0)
    h1 = RandomListNode(1)
    h2 = RandomListNode(2)
    h3 = RandomListNode(3)
    h4 = RandomListNode(4)
    head.next = h1
    h1.next = h2
    h2.next = h3
    h3.next = h4
    head.random = h2
    h1.random = h4
    h2.random = h4
    h3.random = h3

    res = s.Clone(head)
    print res == head
    while res:
        if res.random:
            print res.label, '.random =', res.random.label
        else:
            print res.label, '.random = None'
        res = res.next


