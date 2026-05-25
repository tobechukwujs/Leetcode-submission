class Solution(object):
    def twoSum(self, nums, target):
        value = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in value:
                return [value[diff], i]
            value[num] = i      
              
