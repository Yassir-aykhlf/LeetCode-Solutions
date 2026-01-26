class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = collections.defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(answerKey)):
            freq[answerKey[r]] += 1
            while r - l + 1 - max(freq.values()) > k:
                freq[answerKey[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len