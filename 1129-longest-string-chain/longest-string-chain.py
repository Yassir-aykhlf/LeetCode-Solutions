class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_count = defaultdict(int)
        max_len = 0
        for word in words:
            word_count[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                word_count[word] = max(word_count[word], word_count[pred] + 1)
            max_len = max(max_len, word_count[word])
        return max_len