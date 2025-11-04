class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        return ''.join(char * freq[char] for char in sorted(freq.keys(), key=lambda x: freq[x], reverse=True))