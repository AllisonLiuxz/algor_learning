# -*- coding:utf-8 -*-
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2)时间复杂度，TLE
        """
        if not nums or len(nums) == 1:
            return 0
        print nums
        head, tail = len(nums) - 1, 0
        i, j = 1, len(nums) - 2
        asc_list, dec_list = [nums[0]], [nums[-1]]
        while i < len(nums) and head > 0:
            print "head", head, asc_list
            if nums[i] < asc_list[-1]:
                if nums[i] < asc_list[0]:
                    head = 0
                    break
                else:
                    k = len(asc_list) - 1
                    while k > 0:
                        if nums[i] >= asc_list[k - 1]:
                            asc_list.insert(k, nums[i])
                            break
                        k -= 1
                    head = min(head, k)
            else:
                asc_list.append(nums[i])
            i += 1

        while j > -1 and tail < len(nums)-1:
            print "tail", tail, dec_list
            if nums[j] > dec_list[-1]:
                if nums[j] > dec_list[0]:
                    tail = len(nums) - 1
                    break
                else:
                    k = len(dec_list) - 1
                    while k > 0:
                        if nums[j] <= dec_list[k-1]:
                            dec_list.insert(k, nums[j])
                            break
                        k -= 1
                    tail = max(tail, len(nums) - 1 - k)
            else:
                dec_list.append(nums[j])
            j -= 1
        print "last:", head, tail
        if head <= tail:
            return tail - head + 1
        else:
            return 0
        """

        # 用自己写的快排O(nlogn)，TLE
        """
        def quick_sort(array, low, high):
            if low >= high:
                return
            left = low
            right = high
            key = array[left]
            while left < right:
                while left < right and array[right] >= key:
                    right -= 1
                array[left] = array[right]
                while left < right and array[left] <= key:
                    left += 1
                array[right] = array[left]
            array[right] = key
            quick_sort(array, low, left-1)
            quick_sort(array, left+1, high)

        if not nums or len(nums) == 1:
            return 0

        sort_nums = nums[:]
        quick_sort(sort_nums, 0, len(nums)-1)
        i, j = 0, len(nums)-1
        head, tail = None, None
        while i <= j and (head is None or tail is None):
            if not head:
                if sort_nums[i] == nums[i]:
                    i += 1
                else:
                    head = i
            if not tail:
                if sort_nums[j] == nums[j]:
                    j -= 1
                else:
                    tail = j
        if head is None:
            return 0
        else:
            return tail - head + 1
        """

        # O(n)的复杂度
        if not nums:
            return 0
        head, tail = None, None
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                head = i
                break
        # 判断是否为空，不能用not
        if head is None:
            return 0
        for j in xrange(len(nums)-1, 0, -1):
            if nums[j-1] > nums[j]:
                tail = j
                break
        min_num, max_num = min(nums[head:tail+1]), max(nums[head:tail+1])
        left, right = head, tail
        for k in xrange(head):
            if nums[k] > min_num:
                left = k
                break
        for m in xrange(len(nums) - 1, tail, -1):
            if nums[m] < max_num:
                right = m
                break
        return right - left + 1


if __name__ == '__main__':
    s = Solution()
    # temp = [2, 8, 4, 7, 1, 10]
    # temp = [2, 6, 4, 8, 10, 9, 15]
    # temp = [2, 3, 8, 7, 9, 15, 1]
    # temp = [1, 2, 3, 4]
    # temp = [2, 3, 8, 7, 9, 15, 1]
    # temp = [3, 4, 1, 2, 5]
    # temp = [2, 3, 4, 1, 2, 2, 4, 4]
    temp = [2, 1, 0]
    print s.findUnsortedSubarray(temp)


