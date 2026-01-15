class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1 

        position_index = 0
        for color_index in range(3):
            count = counts[color_index]
            
            for i in range(count):
                nums[position_index] = color_index
                position_index += 1
        return nums
        