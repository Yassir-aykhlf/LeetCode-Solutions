class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        rems = {}
        count = 0
        for t in time:
            rem = (t % 60) % 60
            target = (60 - rem) % 60
            if target in rems:
                count += rems[target]
            rems[rem] = rems.get(rem, 0) + 1
        return count