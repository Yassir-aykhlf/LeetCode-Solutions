class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, _ in sorted(collections.Counter(words).items(), key = lambda tup: (-tup[1], tup[0]))[:k]]