class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        curr_sum = 0
        count = 0
        for n in nums:
            curr_sum += 1 if n % 2 else 0
            target = curr_sum - k
            if target in sum_count:
                count += sum_count[target]
            sum_count[curr_sum] = sum_count.get(curr_sum, 0) + 1
        return count