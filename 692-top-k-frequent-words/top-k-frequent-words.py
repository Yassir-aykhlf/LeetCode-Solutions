class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return sorted(freq.keys(), key=lambda word: (-freq[word], word))[:k]