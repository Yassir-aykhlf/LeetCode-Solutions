class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [0] * n
        for i in range(n):
            for c in words[i]:
                masks[i] |= (1 << (ord(c) - ord('a')))
            lengths[i] = len(words[i])
        prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not masks[i] & masks[j]:
                    prod = max(prod, lengths[i] * lengths[j])
        return prod