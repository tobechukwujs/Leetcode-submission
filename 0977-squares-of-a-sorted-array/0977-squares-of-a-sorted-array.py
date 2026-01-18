class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        position = n - 1 

        while left <= right:
            left_val = nums[left] * nums[left]
            right_val = nums[right] * nums[right]
            
           
            if left_val > right_val:
                result[position] = left_val
                left +=1
            else:
                result[position] = right_val
                right -=1    
          
            position -= 1 
            
        return result  
        