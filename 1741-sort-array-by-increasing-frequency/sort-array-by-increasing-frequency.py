class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        cunt = Counter(nums)
        return sorted(nums, key=lambda x: (cunt[x], -x))
        