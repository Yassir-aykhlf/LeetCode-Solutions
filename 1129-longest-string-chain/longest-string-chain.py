class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        longest_seq = 0
        words.sort(key=len)
        for word in words:
            dp[word] = 1
            for i, c in enumerate(word):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            longest_seq = max(longest_seq, dp[word])
        return longest_seq