class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for n in nums:
            prefix.append(prefix[-1] * n)
        for n in nums[::-1]:
            suffix.append(suffix[-1] * n)
        suffix = suffix[::-1]
        suffix = suffix[1:]
        prefix = prefix[:-1]
        return [i * j for i, j in zip(prefix, suffix)]