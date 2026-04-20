class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res, resultLength = [-1, -1], float('inf')
        left = 0
        
        for r in range(len(s)):
            c =s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have +=1

            while have == need:
                #update results
                if (r - left + 1) < resultLength:
                    res = [left, r]
                    resultLength = (r -left + 1)

                window[s[left]] -=1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1
                left +=1       

        left, r = res
        return s[left:r+1] if resultLength != float('inf') else ""     
        