from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)
        values = list(counts.values()) 
        distinct = set(values)
        
        cof = Counter(values)          
        if len(distinct) >= 3:
            return False
        
        if len(distinct) == 1:
            the_count = next(iter(distinct))      
            return the_count == 1 or len(counts) == 1
        
        c1, c2 = sorted(distinct)           
        if c1 == 1 and cof[1] == 1:   
            return True

        if c2 - c1 == 1 and cof[c2] == 1:
            return True      
        return False   