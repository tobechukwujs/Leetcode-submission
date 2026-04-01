class Solution(object):
    def twoSum(self, nums, target):
        value = {}
        for index, num in enumerate(nums):
            secondValue = target - num
            if secondValue in value:
                return [value[secondValue], index] 
            else:
                value[num] = index       