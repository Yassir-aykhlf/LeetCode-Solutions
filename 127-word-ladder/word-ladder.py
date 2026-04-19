class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        dq = deque([(beginWord, 1)])
        while dq:
            word, turns = dq.popleft()
            if word == endWord:
                return turns
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    perm = word[:i] + c + word[i+1:]
                    if perm in wordSet:
                        wordSet.remove(perm)
                        dq.append((perm, turns + 1))
        return 0