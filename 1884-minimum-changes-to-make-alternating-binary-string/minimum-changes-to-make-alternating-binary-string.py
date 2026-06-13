class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        on = True
        for i in range(len(s)):
            on = not on
            if on and s[i] == '0':
                count1 += 1
            if not on and s[i] == '1':
                count1 += 1
        on = False
        for i in range(len(s)):
            on = not on
            if on and s[i] == '0':
                count2 += 1
            if not on and s[i] == '1':
                count2 += 1
        return min(count1, count2)