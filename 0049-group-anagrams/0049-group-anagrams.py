class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for everyWord in strs:
            count = [0] * 26
            for c in everyWord:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(everyWord)   
        return list(res.values())