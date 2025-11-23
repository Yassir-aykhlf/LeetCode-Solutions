class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        preds = {}
        max_seq = 0
        for word in words:
            preds[word] = 1
            for i in range(len(word)):
                perm = word[:i] + word[i+1:]
                if perm in preds:
                    preds[word] = max(preds[word], preds[perm] + 1)
            max_seq = max(max_seq, preds[word])
        return max_seq