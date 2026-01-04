class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            l = 0
            counter = 0
            freq = collections.defaultdict(int)
            for r in range(len(nums)):
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                counter += r - l + 1
            return counter
        return atMost(k) - atMost(k - 1)