class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        chains = {}
        longest_chain = 0
        for word in words:
            chains[word] = 1
            for i, c in enumerate(word):
                perm = word[:i] + word[i+1:]
                if perm in chains:
                    chains[word] = max(chains[word], chains[perm] + 1)
            longest_chain = max(longest_chain, chains[word])
        return longest_chain