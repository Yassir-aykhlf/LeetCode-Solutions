class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = {}
        count = 0
        for t in time:
            rem = t % 60
            com = (60 - rem) % 60
            if com in rems:
                count += rems[com]
            rems[rem] = rems.get(rem, 0) + 1
        return count