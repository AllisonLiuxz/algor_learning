# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data or len(data) <= 1:
            return 0
        global res
        res = 0

        def merge_sort_count(ll):
            if not ll:
                return
            if len(ll) == 1:
                return ll
            mid = len(ll) / 2
            left = merge_sort_count(ll[:mid])
            right = merge_sort_count(ll[mid:])
            i, j = 0, 0
            tmp = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    tmp.append(left[i])
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
                    global res
                    res += len(left[i:])
            if i == len(left):
                tmp += right[j:]
            else:
                tmp += left[i:]
            return tmp
        merge_sort_count(data)
        return res % 1000000007


if __name__ == '__main__':
    s = Solution()
    # input_list = [1, 3, 7, 8, 2, 4, 6, 5]
    input_list = [1, 2, 3, 4, 5, 6, 7, 0]
    print s.InversePairs(input_list)
