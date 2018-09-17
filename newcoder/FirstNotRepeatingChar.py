# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        find_dict = {}
        for i in range(len(s)):
            if s[i] in find_dict:
                del find_dict[s[i]]
            else:
                find_dict[s[i]] = i
        if not find_dict:
            return -1
        res = len(s) - 1
        for index in find_dict.values():
            if index < res:
                res = index
        return res

if __name__ == '__main__':
    s = Solution()
    temp = 'googgle'
    print s.FirstNotRepeatingChar(temp)
