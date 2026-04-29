class Solution:
    def decodeString(self,s):
        stack = []
        currNum = 0
        currStr = ''
        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            elif char == '[':
                stack.append([currStr, currNum])
                currNum = 0
                currStr = ''
            elif char == ']':
                prevStr, prevNum = stack.pop()
                currStr = prevStr + (prevNum * currStr)
            else:
                currStr +=char 
        return currStr       