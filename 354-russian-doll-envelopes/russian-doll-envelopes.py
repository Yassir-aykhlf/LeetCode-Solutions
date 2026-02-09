class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Longest Increasing Subsequence
        for Heights, because Widths are
        garenteed to be sorted, the issue
        and tie breaker is the Height
        the LIS of Heights is the longest
        possible increasing chain: LIS
        How to implement LIS?
        [ ] -> keep adding best canditates
        best canditates: smaller than the largest
        Binary Search? why? Bisect right or left?
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        heights = [h for _, h in envelopes]
        LIS = []
        for h in heights:
            # bisect right to append to the seq?
            prev_h_idx = bisect.bisect_left(LIS, h)
            if prev_h_idx == len(LIS):
                LIS.append(h)
            else:
                LIS[prev_h_idx] = h
        return len(LIS)