class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        preds = collections.defaultdict(int)
        max_seq = 1
        for word in words:
            preds[word] = 1
            for i, c in enumerate(word):
                prev = word[:i] + word[i+1:]
                preds[word] = max(preds[word], preds[prev] + 1)
            max_seq = max(max_seq, preds[word])
        return max_seq