class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        max_len = 0
        preds = collections.defaultdict(int)
        for word in words:
            preds[word] = 1
            for i, c in enumerate(word):
                pred = word[:i] + word[i + 1: ]
                preds[word] = max(preds[word], preds[pred] + 1)
            max_len = max(max_len, preds[word])
        return max_len