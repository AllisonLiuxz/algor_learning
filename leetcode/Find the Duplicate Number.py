class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        i, j = 0, nums[0]
        while nums[i] != nums[j]:
            i = nums[i]
            j = nums[nums[j]]
        i = 0
        j = nums[j]
        while nums[i] != nums[j]:
            i = nums[i]
            j = nums[j]
        return nums[i]


if __name__ == "__main__":
    s = Solution()
    # temp = [1, 3, 4, 2, 2]
    # temp = [3, 1, 3, 4, 2]
    temp = [1, 2, 3, 1, 1, 1, 4, 6]
    print s.findDuplicate(temp)
