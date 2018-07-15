# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV or len(pushV) != len(popV):
            return False
        m, n = 0, 0
        tmp_stack = []
        while m < len(pushV) and n < len(popV):
            if pushV[m] == popV[n]:
                m += 1
                n += 1
                while n < len(popV) and tmp_stack and tmp_stack[-1] == popV[n]:
                    tmp_stack.pop()
                    n += 1
            else:
                tmp_stack.append(pushV[m])
                m += 1
        if len(tmp_stack) == m-n and popV[n:] == tmp_stack[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print test.IsPopOrder([1, 2, 3, 4, 5], [2, 4, 5, 3, 1])
    print test.IsPopOrder([1, 2, 3, 4, 5], [2, 4, 5, 1, 3])
