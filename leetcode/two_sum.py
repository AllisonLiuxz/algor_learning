def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
	        left_num = target - nums[i]
	        # print (dic.get(left_num,None) is not None), dic.get(left_num,None) != i
	        if (dic.get(left_num,None) is not None) and dic.get(left_num,None) != i:
	            return [dic[left_num],i]
	        dic[nums[i]] = i
        return None

test = [0,4,3,0]
print twoSum(test,0)
