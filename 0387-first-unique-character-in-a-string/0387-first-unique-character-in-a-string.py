class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}

        for char in s:
    #look through every letter and then increase count, if the letter has been seen before
            if char in letters:
                letters[char] +=1

            else:
                letters[char] =1
        for i in range(len(s)): 
            if letters[s[i]]== 1:
                return i  

        return -1         
      