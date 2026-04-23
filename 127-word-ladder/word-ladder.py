class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        dq = deque([(beginWord, 0)])
        while dq:
            prev_word, seq_len = dq.popleft()
            if prev_word == endWord:
                return seq_len + 1
            for i in range(len(prev_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = prev_word[:i] + c + prev_word[i+1:]
                    if new_word in wordSet:
                        dq.append((new_word, seq_len + 1))
                        wordSet.remove(new_word)
        return 0