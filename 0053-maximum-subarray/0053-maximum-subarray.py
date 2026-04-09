class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum = max(num, current_sum + num)
            if current_sum > max_sum:
                max_sum = max(max_sum, current_sum)
        return max_sum
        