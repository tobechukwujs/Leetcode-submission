class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum = 0
        count = 0
        prefixSum = {0: 1}
        
        for num in nums:
            runningSum += num
            if runningSum - k in prefixSum:
                count += prefixSum[runningSum - k]
            prefixSum[runningSum] = prefixSum.get(runningSum, 0) + 1
        return count