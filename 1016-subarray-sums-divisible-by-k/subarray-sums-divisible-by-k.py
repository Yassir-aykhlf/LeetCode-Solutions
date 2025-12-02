class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rems = {0:1}
        count = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            rem = cur_sum % k
            if rem in rems:
                count += rems[rem]
            rems[rem] = rems.get(rem, 0) + 1
        return count