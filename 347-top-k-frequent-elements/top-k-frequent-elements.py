class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])