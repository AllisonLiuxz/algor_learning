# -*- coding:utf-8 -*-
from collections import defaultdict
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        d = defaultdict(lambda: 0)
        for num in numbers:
            d[num] += 1
        tmp = 0
        print d
        for num in d:
            if d[num] > tmp:
                tmp = d[num]
                res = num
        if tmp > len(numbers)/2:
            return res
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1]
    print s.MoreThanHalfNum_Solution(nums)
