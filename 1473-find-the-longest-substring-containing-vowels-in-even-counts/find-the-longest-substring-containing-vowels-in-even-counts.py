class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        seen = {0: -1}
        state = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in vowels:
                state ^= (1 << vowels[c])
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i
        return max_len