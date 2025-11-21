class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rems = {0: 1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            rem = cur_sum % k
            if rem in rems:
                count += rems[rem]
            rems[rem] = rems.get(rem, 0) + 1
        return count