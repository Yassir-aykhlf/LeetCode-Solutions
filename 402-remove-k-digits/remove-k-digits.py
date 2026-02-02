class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while stack and k:
            stack.pop()
            k -= 1
        res = ''.join(stack).lstrip('0')
        return res if res else "0"