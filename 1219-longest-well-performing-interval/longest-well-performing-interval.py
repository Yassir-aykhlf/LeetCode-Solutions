class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = {0: -1}
        max_len = 0
        curr = 0
        for i, hour in enumerate(hours):
            curr += 1 if hour > 8 else -1
            if curr > 0:
                max_len = i + 1
            elif (curr - 1) in prefix_sum:
                max_len = max(max_len, i - prefix_sum[curr - 1])
            if curr not in prefix_sum:
                prefix_sum[curr] = i
        return max_len