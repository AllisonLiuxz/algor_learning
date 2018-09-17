# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        max_sum, tmp = array[0], array[0]
        for num in array[1:]:
            if tmp > 0 and tmp + num >= 0:
                tmp += num
            else:
                tmp = num
            max_sum = max(max_sum, tmp)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    # input_array = [6, -3, -2, 7, -15, 1, 2, 2]
    # input_array = [-5, -3, 0, -1, -5]
    input_array = []
    print s.FindGreatestSumOfSubArray(input_array)