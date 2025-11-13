class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # the smallest positive integer that could be missing is 1 
        # the biggest  positive integer that could be missing is n+1
        # the answer must be in range [1, n+1]
        # therefore numbers <= 0 or > n,
        # are useless, they can never be the answer
        # let's clean the array of useless numbers,
        # by replacing them with a positive value we always ignore: n + 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # the insight is to use the indices as our hash set
        # for each number,
        # we mark its presence with making nums[num - 1] negative
        # so when we iterate and find a positive value,
        # it means the value at this index was never flipped,
        # never marked, index + 1 was never seen
        # we are leveraging the sequential positive nature of indices
        # to solve this problem
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        # Now we iterate to detect
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # no value in [1, n] is missing,
        # therefore the closest missing value is n + 1
        return n + 1