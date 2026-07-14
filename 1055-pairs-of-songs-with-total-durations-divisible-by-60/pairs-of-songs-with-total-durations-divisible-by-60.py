class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        rems = {}
        for t in time:
            rem = t % 60
            tar = (60 - rem) % 60
            if tar in rems:
                count += rems[tar]
            rems[rem] = rems.get(rem, 0) + 1
        return count