class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # [9,9,6,0,6,6,9] => [1,1,-1,-1,-1,-1,1] because we don't care about the values, we care about the condition: h > 8
        # why -1 and not 0? ...
        curr = 0
        longest = 0
        prefix = {0: -1}
        for i, h in enumerate(hours):
            curr += 1 if h > 8 else -1
            if curr > 0:
                longest = i + 1
            elif (curr - 1) in prefix:
                longest = max(longest, i - prefix[curr - 1])
            if curr not in prefix:
                prefix[curr] = i
        return longest