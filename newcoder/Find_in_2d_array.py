# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or not array[0]:
            return None
        if array[0][0] > target or array[-1][-1] < target:
            return False
        col_start = 0
        col_end = len(array) - 1
        row_start = 0
        row_end = len(array[0]) - 1
        flag = True
        while col_start < col_end and row_start < row_end:
            if flag:
                for i in range(col_start, col_end + 1):
                    if array[i][row_start] == target:
                        return True
                    if array[i][row_start] > target:
                        col_end = i - 1
                        break
                for j in range(row_start, row_end + 1):
                    if array[col_start][j] == target:
                        return True
                    if array[col_start][j] > target:
                        row_end = j - 1
                        break

                flag = False
            else:
                for i in range(col_end, col_start - 1, -1):
                    if array[i][row_end] == target:
                        return True
                    if array[i][row_end] < target:
                        col_start = i + 1
                        break
                for j in range(row_end, row_start - 1, -1):
                    if array[col_end][j] == target:
                        return True
                    if array[col_end][j] < target:
                        row_start = j + 1
                        break
                flag = True
            if array[col_end][row_end] < target:
                return False
        return False
