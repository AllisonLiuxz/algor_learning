# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        count = dict()
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for n in range(len(s)):
            if count[s[n]] == 1:
                return n
        return -1


if __name__ == '__main__':
    s = Solution()
    temp = 'abcba'
    print s.FirstNotRepeatingChar(temp)