class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        items = sorted(freq.items(), key = lambda tup: (-tup[1], tup[0]))[:k]
        return [name for name, _ in items]