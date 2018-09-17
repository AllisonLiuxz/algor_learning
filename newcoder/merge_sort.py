# -*- coding:utf-8 -*-
class Solution:
    def MergeSort(self, data):
        # write code here
        if not data:
            return None
        if len(data) == 1:
            return data
        mid = len(data) / 2
        left = self.MergeSort(data[:mid])
        right = self.MergeSort(data[mid:])
        tmp = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        if i == len(left):
            tmp += right[j:]
        else:
            tmp += left[i:]
        return tmp


if __name__ == '__main__':
    s = Solution()
    input_list = [1, 5, 3, 2, 4, 7, 8, 0]
    print s.MergeSort(input_list)
