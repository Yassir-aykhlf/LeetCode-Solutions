class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        dq = deque([(beginWord, 1)])
        while dq:
            word, seq_len = dq.popleft()
            if word == endWord:
                return seq_len
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    perm = word[:i] + c + word[i+1:]
                    if perm in wordSet:
                        dq.append((perm, seq_len + 1))
                        wordSet.remove(perm)
        return 0