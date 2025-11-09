class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0:-1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in remainders:
                if i - remainders[cur_rem] > 1:
                    return True
            else:
                remainders[cur_rem] = i
        return False