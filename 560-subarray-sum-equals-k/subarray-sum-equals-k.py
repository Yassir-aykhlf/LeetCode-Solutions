class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixs = {0: 1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefixs:
                count += prefixs[cur_sum - k]
            prefixs[cur_sum] = prefixs.get(cur_sum, 0) + 1
        return count