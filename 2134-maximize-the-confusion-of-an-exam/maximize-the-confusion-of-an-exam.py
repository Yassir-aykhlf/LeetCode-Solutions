class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = defaultdict(int)
        max_len = 0
        max_count = 0
        l = 0
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1
            max_count = max(max_count, count[answerKey[r]])
            while (r - l + 1) - max_count > k:
                count[answerKey[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len