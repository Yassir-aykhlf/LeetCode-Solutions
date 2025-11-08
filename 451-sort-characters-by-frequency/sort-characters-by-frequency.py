class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        return ''.join(char * freq[char] for char in sorted(freq.keys(), key=lambda x:freq[x], reverse=True))