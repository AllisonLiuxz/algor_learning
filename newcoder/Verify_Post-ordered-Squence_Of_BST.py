# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        print sequence
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        if len(sequence) == 2:
            return True
        s_list, l_list = [], []
        key = sequence[-1]
        flag = 0
        for i in range(len(sequence)-1):
            if sequence[i] < key:
                if flag:
                    return False
                else:
                    s_list.append(sequence[i])
            else:
                flag = 1
                l_list.append(sequence[i])
        if not s_list:
            return self.VerifySquenceOfBST(l_list)
        if not l_list:
            return self.VerifySquenceOfBST(s_list)
        return self.VerifySquenceOfBST(s_list) and self.VerifySquenceOfBST(l_list)

if __name__ == '__main__':
    s = Solution()
    print s.VerifySquenceOfBST([2,9,5,16,17,15,19,18,12])
