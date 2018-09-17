# —*- coding:utf-8 -*-
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 动态规划：O(n2)的时间复杂度，O(n2)的空间复杂度
        """
        if not s:
            return 0

        n = len(s)
        res = n
        D = [[0] * x + [1] + [0]*(n-x-1) for x in xrange(n)]
        
        # # 动规的顺序很重要，要从矩阵对角线向外填，所以这种循环方式不正确
        # for i in xrange(n-1):
        #     for j in xrange(i+1, n):
        #         if j-i == 1:
        #             # 用int()将True,False转换为 1，0
        #             D[i][j] = int(s[i] == s[j])
        #         else:
        #             D[i][j] = int(s[i] == s[j] and D[i+1][j-1])
        #         res += D[i][j]
        
        for j in xrange(1, n):
            # 从对角线出发，向边界靠近
            for i in xrange(j-1, -1 ,-1):
                if j - i == 1:
                    # 用int()将True,False转换为 1，0
                    D[i][j] = int(s[i] == s[j])
                else:
                    D[i][j] = int(s[i] == s[j] and D[i + 1][j - 1])
                res += D[i][j]

        return res
        """

        # 利用回文的对称性，时间O(n2)，空间O(1)
        if not s:
            return 0
        i, res = 0, 0
        while 0 <= i < len(s):
            # 奇数长的字符串
            left, right = i, i
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # 偶数长的字符串
            left, right = i, i+1
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    temp = 'abc'   # 3
    # temp = 'abac'   # 5
    # temp = 'aaa'   # 6
    # temp = 'abcbc'   # 7
    # temp = 'a'   # 1
    # temp = ''   # 0
    # temp = 'ababa'    # 9
    # temp = 'abababa'   # 16

    print s.countSubstrings(temp)