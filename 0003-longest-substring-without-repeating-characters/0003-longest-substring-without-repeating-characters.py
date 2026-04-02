class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        result = 0
        for right, char in enumerate(s):
            if char in map and map[char] >= left:
                left = map[char]+1
            map[char] = right
            result = max(result, right - left + 1)
        return result        

        