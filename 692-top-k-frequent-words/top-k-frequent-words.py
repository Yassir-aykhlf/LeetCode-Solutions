class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        return heapq.nsmallest(k, freq.keys(), key=lambda x: (-freq[x], x))