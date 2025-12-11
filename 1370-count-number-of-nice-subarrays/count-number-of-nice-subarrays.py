class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # the property we care about is parity, so we can ignore the values
        # and replace the value of odd numbers with 1, and even numbers with 0
        # [1,1,2,1,1] => [1,1,0,1,1]
        # k odd numbers subarray is a subarray with the sum equal to k
        # rendering this problem a simple "subarray sum equals k" problem
        prefix = {0: 1}
        curr = 0
        count = 0
        for num in nums:
            curr += 1 if num % 2 != 0 else 0
            target = curr - k
            if target in prefix:
                count += prefix[target]
            prefix[curr] = prefix.get(curr, 0) + 1
        return count