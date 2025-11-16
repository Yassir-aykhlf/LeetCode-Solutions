class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = {}
        count = 0
        for t in time:
            rem = t % 60
            target_rem = (60 - rem) % 60
            if target_rem in remainders:
                count += remainders[target_rem]
            remainders[rem] = remainders.get(rem, 0) + 1
        return count