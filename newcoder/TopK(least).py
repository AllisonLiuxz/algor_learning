# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        if k == len(tinput):
            return sorted(tinput)

        def max_heap(heap, pos, n):
            cur = pos
            left = pos * 2 + 1
            right = pos * 2 + 2
            if left < n and heap[cur] < heap[left]:
                cur = left
            if right < n and heap[cur] < heap[right]:
                cur = right
            if cur != pos:
                heap[cur], heap[pos] = heap[pos], heap[cur]
                max_heap(heap, cur, n)
            return heap

        def build_max_heap(ll):
            for n in range(len(ll)/2-1, -1, -1):
                max_heap(ll, n, len(ll))
            return ll

        tinput[:k] = build_max_heap(tinput[:k])
        for i in range(k, len(tinput)):
            if tinput[i] < tinput[0]:
                tinput[0], tinput[i] = tinput[i], tinput[0]
                tinput[:k] = max_heap(tinput[:k], 0, k)
        return sorted(tinput[:k])

if __name__ == '__main__':
    s = Solution()
    tmp = [4, 5, 1, 6, 2, 7, 3, 8]
    print s.GetLeastNumbers_Solution(tmp, 8)