class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        for num in numbers:
            totalSum = numbers[l] + numbers[r] 
            if totalSum > target:
                r -= 1
            elif totalSum < target:
                l += 1
        return [l+1, r+1]             