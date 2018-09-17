# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []

        def gen_permutation(s):
            if not s:
                return None
            if len(s) == 1:
                return [s]
            tmp = []
            for i in range(len(s)):
                per = gen_permutation(s[:i]+s[i+1:])
                for p in per:
                    tmp.append(s[i]+p)
            return tmp
        res = sorted(list(set(gen_permutation(ss))))
        return res

if __name__ == '__main__':
    s = Solution()
    string = 'Bacb'
    print s.Permutation(string)
