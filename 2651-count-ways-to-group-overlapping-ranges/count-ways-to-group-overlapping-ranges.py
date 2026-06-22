class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort()
        last_end = ranges[0][1]
        total_chunks = 1
        for start, end in ranges[1:]:
            if start > last_end:
                total_chunks += 1
            last_end = max(last_end, end)
        return pow(2, total_chunks, mod)