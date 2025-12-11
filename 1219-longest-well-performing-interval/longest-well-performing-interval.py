class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # [9,9,6,0,6,6,9] => [1,1,-1,-1,-1,-1,1] because we don't care about the values, we care about the condition: h > 8
        # why -1 and not 0? because we want to find an interval with strict positive sum, each low performing day negatively affect the score
        # we also care about the "velocity" rather than the score, so if we have already seen (curr - 1) it means we are going up, therefore having more productive days, and since we are looking for the longest productive window curr - 1 yeilds the farthest one
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