class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = Counter(s)
        return ''.join([char * freqMap[char] for char in sorted(freqMap.keys(), key=lambda x:freqMap[x], reverse=True)])