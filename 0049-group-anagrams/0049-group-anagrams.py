class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for everyWord in strs:
            count = [0] * 26
            # this code creates multiple 0, 26 to be specific, which we can mimic as a-z
            for c in everyWord:
                count[ord(c)-ord('a')] +=1
                 #the code just says when you see a word lik a, put the count in the first 0, like [1,0 0 ...], and  the , #'' is to make python know its a string
            res[tuple(count)].append(everyWord)   
            #convets the 26list into a tuple, then append every word to that key it ,matches
        return list(res.values())