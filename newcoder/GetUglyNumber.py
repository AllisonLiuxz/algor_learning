# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return None
        if index == 1:
            return 1

        def insert_list(wl, num):
            if not wl:
                wl = [num]
                return wl
            if num == wl[-1]:
                return wl
            if num < wl[0]:
                wl.insert(0, num)
                return wl
            if num > wl[-1]:
                wl.append(num)
                return wl
            for i in range(len(wl)-1):
                if wl[i] == num:
                    return wl
                if wl[i] < num < wl[i+1]:
                    wl.insert(i+1, num)
                    return wl

        ugly = [1]
        wait_list = []
        while index-1:
            # print '*2:', wait_list
            wait_list = insert_list(wait_list, ugly[-1] * 2)
            # print '*3:', wait_list
            wait_list = insert_list(wait_list, ugly[-1] * 3)
            # print '*5:', wait_list
            wait_list = insert_list(wait_list, ugly[-1] * 5)
            # print 'ugly:', ugly, 'wait:', wait_list
            ugly.append(wait_list.pop(0))
            index -= 1
            # print ugly[-1]
        return ugly[-1]


if __name__ == '__main__':
    s = Solution()
    temp = 14
    print s.GetUglyNumber_Solution(temp)
