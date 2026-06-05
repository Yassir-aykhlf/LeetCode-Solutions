class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for n in nums:
            if n < 10:
                digit_sum += n
            else:
                while n:
                    n, d = divmod(n, 10)
                    digit_sum += d
        return element_sum - digit_sum