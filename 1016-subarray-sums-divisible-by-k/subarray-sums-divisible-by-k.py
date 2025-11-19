class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = {0: 1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            rem = cur_sum % k
            if rem in remainder:
                count += remainder[rem]
            remainder[rem] = remainder.get(rem, 0) + 1
        return count