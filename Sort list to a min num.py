# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if (str(numbers[i]) + str(numbers[j])) > (str(numbers[j]) + str(numbers[i])):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        res = ''
        for n in numbers:
            res += str(n)
        return int(res)

if __name__ == '__main__':
    s = Solution()
    input_list = [3, 329, 32]
    print s.PrintMinNumber(input_list)