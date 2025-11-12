class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        count = 0
        for t in time:
            rem = t % 60
            partner_rem = (60 - rem) % 60
            count += remainders[partner_rem]
            remainders[rem] += 1
        return count