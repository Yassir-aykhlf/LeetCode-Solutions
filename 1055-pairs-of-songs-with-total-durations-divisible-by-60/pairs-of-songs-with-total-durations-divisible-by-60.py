class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = {}
        count = 0
        for t in time:
            curr = t % 60 
            tar = (60 - curr) % 60
            if tar in rems:
                count += rems[tar]
            rems[curr] = rems.get(curr, 0) + 1
        return count