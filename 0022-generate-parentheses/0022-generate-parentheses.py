class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(current_string, open_count, close_count):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            if open_count < n:
                generate(current_string + "(", open_count + 1, close_count)
            if close_count < open_count:
                generate(current_string + ")", open_count, close_count + 1)
        generate("", 0, 0)
        return result            