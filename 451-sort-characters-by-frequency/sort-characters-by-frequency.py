class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(char * freq for char, freq in sorted(freq.items(), key=itemgetter(1), reverse=True))