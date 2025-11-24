class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rems = {0: 1}
        cur_sum, count = 0, 0
        for num in nums:
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in rems:
                count += rems[cur_rem]
            rems[cur_rem] = rems.get(cur_rem, 0) + 1
        return count