class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        seen_scores = {}
        curr_score = 0
        max_len = 0
        for i, h in enumerate(hours):
            curr_score += 1 if h > 8 else -1
            if curr_score > 0:
                max_len = i + 1
            else:
                if (curr_score - 1) in seen_scores:
                    max_len = max(max_len, i - seen_scores[curr_score - 1])
            if curr_score not in seen_scores:
                seen_scores[curr_score] = i
        return max_len