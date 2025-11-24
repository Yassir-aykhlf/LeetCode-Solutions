class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_index = {0: -1}
        cur_sum, count = 0, 0
        for i, num in enumerate(nums):
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in rem_index:
                if i - rem_index[cur_rem] >= 2:
                    return True
            else:
                rem_index[cur_rem] = i
        return False 