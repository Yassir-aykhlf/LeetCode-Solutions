class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        curr = 0
        max_len = 0
        prefix = {0: -1}
        for i, hour in enumerate(hours):
            curr += 1 if hour > 8 else -1
            if curr > 0:
                max_len = max(max_len, i + 1)
            elif (curr - 1) in prefix:
                max_len = max(max_len, i - prefix[curr - 1])
            if curr not in prefix:
                prefix[curr] = i
        return max_len