class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0:-1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem not in remainders:
                remainders[cur_rem] = i
            elif i - remainders[cur_rem] >= 2:
                return True
        return False