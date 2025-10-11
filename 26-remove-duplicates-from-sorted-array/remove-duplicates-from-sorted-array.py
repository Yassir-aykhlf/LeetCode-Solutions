class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1
        # start for index 1 because the first is always unique
        for read in range(1, len(nums)):
            # if we the current number is unique, write it
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
            # else keep searching for the next unique item
        # return the index after the last unique item,
        # which is also the length of the unique string
        return write