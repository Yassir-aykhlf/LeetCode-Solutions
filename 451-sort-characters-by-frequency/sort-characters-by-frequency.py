class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(c * f for c, f in sorted(freq.items(), key=itemgetter(1), reverse=True))