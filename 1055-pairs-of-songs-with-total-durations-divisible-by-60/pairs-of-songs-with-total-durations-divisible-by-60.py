class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # pair is divisible by 60 if: sum(pair) % 60 == 0
        # for each time we identify the complimenting pair, and see if we have seen one before
        # if so, we can form pairs equal to how many time we have seen a number that it remainder is a valid pair
        # num1 % 60 = 0; num2 % 60 = 0, sum(num1, num2) % = 60
        remainders = defaultdict(int)
        # {rem: count_of_numbers_that_give_this_remainder}
        count = 0
        for t in time:
            rem = t % 60
            target_pair = (60 - t) % 60
            # t + t_p = 60; we are looking for a pair-remainder
            # the % 60 is to insure the result remains in range [0, 59]
            count += remainders[target_pair]
            remainders[rem] += 1
        return count