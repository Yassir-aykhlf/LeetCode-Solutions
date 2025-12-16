class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rems = {0: 1}
        count = 0
        cur = 0
        for num in nums:
            cur += num
            rem = cur % k
            if rem in rems:
                count += rems[rem]
            rems[rem] = rems.get(rem, 0) + 1
        return count