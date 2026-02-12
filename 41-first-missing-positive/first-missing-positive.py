"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 0 is not considered positive
        # the first positive is 1
        # we are looking for the first missing positive
        # nums_ = set(nums)
        # for n in range(1, max(nums_)):
        #     if n not in nums_:
        #         return n
        # return max(nums_) + 1
        # the time complexity is O(max(arr))
        # can we do O(n)?
        # a smart, unhuman insight is that we only care about number between 1 and n
        # huh how is that
        # well if we have the array [2, 1000] all numbers between 2 and 1000 are irrelevant
        # the only relevent numbers are 1, 2 and 3, which all fall in the range [1, n + 1]
        # let's do that again, [3,4,-1,1], let's mark the irrelevance: [3,4,x,1]
        # the range becomes [1, 5], if -1 was 2 the answer would've been n + 1 = 5
        n = len(nums)
        for i in range(n):
            if nums[i] > n or nums[i] < 1:
                nums[i] = n + 1
        # now that we marked the irrelevant numbers with our maximum possible answer
        # we know that all of the number in the range [1, n + 1]
        # meaning we can mark the index n - 1 for every n in nums
        # [3,4,-1,1] becomes [3, 4, 5, 1] becomes [-3, 4, -5, -1], 5 -> index 4 -> ignore
        # notice how 4 is unmarked because it is in index 1, which requires the presence of num 2
        # bingo! 2 is the missing number
        for i in range(n):
            index = abs(nums[i]) - 1
            if index < n and index >= 0:
                if nums[index] > 0:
                    nums[index] *= -1
        # loop, detect the first unmarked (positive), return its index + 1
        print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # else if all is marked the answer is n + 1
        return n + 1