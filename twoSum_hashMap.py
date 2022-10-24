class Solution(object):
    def twoSum(self, nums, target): 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """This is a solution of O(1) using hashmaps"""
        save = []
        nums_map ={}
        diff = 0
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in nums_map:
                nums_map[n] = i
            else:
                return(i,nums_map[diff])
        return save
