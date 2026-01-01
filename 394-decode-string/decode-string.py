class Solution:
    def decodeString(self, s: str) -> str:
        string = ""
        stack = []
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
                count = stack.pop()
                segm = stack.pop()
                string = segm + count * string
        return string