class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        count = 0
        cur = 0
        for r in range(len(nums)):
            cur += 1 if nums[r] % 2 == 1 else 0
            tar = cur - k
            if tar in prefix:
                count += prefix[tar]
            prefix[cur] = prefix.get(cur, 0) + 1
        return count