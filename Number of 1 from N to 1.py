# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        length = len(str(n))
        num = '0' + str(n) + '0'
        res = 0
        for i in range(1, length+1):
            if num[i] == '0':
                res += 10 ** (length-i) * int(num[:i])
            elif num[i] == '1':
                res += 10 ** (length - i) * int(num[:i]) + 1
                if i < length:
                    res += int(num[i+1:-1])
            else:
                res += 10 ** (length-i) * int(num[:i]) + 10 ** (length-i)
        return res

if __name__ == '__main__':
    s = Solution()
    input_num = 100
    print s.NumberOf1Between1AndN_Solution(input_num)
