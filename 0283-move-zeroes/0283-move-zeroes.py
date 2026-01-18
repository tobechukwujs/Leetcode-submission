class Solution(object):
    def moveZeroes(self, nums):
        writer = 0
        for num in nums:
            if num != 0:
                nums[writer] = num
                writer += 1
        for num in range (writer, len(nums)):
            nums[writer] = 0
            writer +=1

        return nums           
