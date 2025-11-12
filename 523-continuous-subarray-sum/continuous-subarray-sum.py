class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = collections.defaultdict(int)
        prefix[0] = -1
        cur_sum = 0
        count = 0
        for i, num in enumerate(nums):
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in prefix:
                if i - prefix[cur_rem] >= 2:
                    return True
            else:
                prefix[cur_rem] = i
        return False