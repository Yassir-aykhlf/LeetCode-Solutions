class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                string += c
            elif c == '[':
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif c == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                string = prev_str + prev_num * string
        return string