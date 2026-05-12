class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for current in intervals:
            if merged and merged[-1][-1] >= current[0]:
                merged[-1][-1] = max(merged[-1][-1], current[-1])
            else:
                merged.append(current)
        return merged           