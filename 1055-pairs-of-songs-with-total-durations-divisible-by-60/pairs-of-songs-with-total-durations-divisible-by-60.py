class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = {}
        cur_sum = 0
        count = 0
        for t in time:
            rem = t % 60
            tar_rem = (60 - rem) % 60
            if tar_rem in rems:
                count += rems[tar_rem]
            rems[rem] = rems.get(rem, 0) + 1
        return count