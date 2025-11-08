class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        return ''.join(char * count for char, count in sorted(freq.items(), key=itemgetter(1), reverse=True))