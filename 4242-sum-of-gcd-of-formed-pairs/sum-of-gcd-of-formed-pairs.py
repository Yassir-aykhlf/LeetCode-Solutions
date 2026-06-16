class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = [0] * len(nums) 
        max_ = 0
        for i in range(len(nums)):
            max_ = max(max_, nums[i])
            prefixGcd[i] = math.gcd(nums[i], max_)
        prefixGcd.sort()
        sum_ = 0
        i, j = 0, len(nums) - 1
        while i < j:
            sum_ += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        return sum_