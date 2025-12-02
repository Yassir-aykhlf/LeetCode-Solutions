class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rems = {0: -1}
        count = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            rem = cur_sum % k
            if rem in rems:
                if r - rems[rem] >= 2:
                    return True
            else:
                rems[rem] = r
        return False