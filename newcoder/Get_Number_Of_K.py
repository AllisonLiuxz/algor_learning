# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data or not k:
            return None
        left, right = 0, len(data)
        while left <= right and data[left] <= k <= data[right]:
            mid = (left + right) / 2
            if data[mid] == k:
                break
            if 