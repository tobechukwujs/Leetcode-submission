class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for currentInterval in intervals:
            if merged and merged[-1][-1] >= currentInterval[0]:
                merged[-1][-1] = max(merged[-1][-1], currentInterval[-1])
            else:
                merged.append(currentInterval)
        return merged
                

