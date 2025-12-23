class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            freq = defaultdict(int)
            max_len = 0
            l = 0
            total = 0
            for r in range(len(nums)):
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                total += r - l + 1
            return total
        return atMostK(k) - atMostK(k - 1)