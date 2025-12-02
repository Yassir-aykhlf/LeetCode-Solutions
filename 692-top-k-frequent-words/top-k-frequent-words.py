class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        tuples = list(freq.items())
        return [w for w, f in sorted(tuples, key = lambda t: (-t[1], t[0]))[:k]]