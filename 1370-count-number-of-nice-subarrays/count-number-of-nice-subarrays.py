class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        count = 0
        curr = 0
        for num in nums:
            curr += 1 if num % 2 == 1 else 0
            diff = curr - k
            if diff in prefix:
                count += prefix[diff]
            prefix[curr] = prefix.get(curr, 0) + 1
        return count