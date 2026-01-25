class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                string += c
            elif c == '[':
                stack.append(string)
                stack.append(num)
                num = 0
                string = ""
            elif c == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                string = prev_str + string * int(prev_num)
        return string