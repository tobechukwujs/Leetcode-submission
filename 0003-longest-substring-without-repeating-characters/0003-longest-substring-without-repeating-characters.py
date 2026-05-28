class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        best = 0
        for i, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char]+1)
            seen[char] = i    
            best = max(best, i - left +1) 
        return best           
