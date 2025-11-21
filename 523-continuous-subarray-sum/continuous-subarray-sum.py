class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rems = {0: -1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            rem = cur_sum % k
            if rem in rems:
                if i - rems[rem] >= 2:
                    return True
            else:
                rems[rem] = i
        return False