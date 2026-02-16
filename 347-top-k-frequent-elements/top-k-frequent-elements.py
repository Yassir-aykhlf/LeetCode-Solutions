class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]