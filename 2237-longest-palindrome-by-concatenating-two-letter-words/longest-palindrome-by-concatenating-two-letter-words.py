class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        state = Counter(words)
        oddy_exists = False
        res = 0
        used = False
        for w, freq in state.items():
            if w[0] == w[1]:
                if freq % 2:
                    oddy_exists = True
                res += (freq // 2) * 4
            else:
                res += min(freq, state[w[::-1]]) * 2
        res += 2 if oddy_exists else 0
        return res