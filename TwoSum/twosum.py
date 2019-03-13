class Solution:
    def twoSum(self, nums, target):
        res = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in res:
                return [res[temp],i]
            else:
                res[nums[i]] = i
                #class Solution(object):
                def twoSum(self, nums, target):
                        """
                        :type nums: List[int]
                        :type target: int
                        :rtype: List[int]
                        """
                        l = len(nums)
                        for i in range(l):
                            for j in range(l):
                                if i != j and nums[i]+nums[j] == target:
                                    return [i,j]
                        return [] 
                    