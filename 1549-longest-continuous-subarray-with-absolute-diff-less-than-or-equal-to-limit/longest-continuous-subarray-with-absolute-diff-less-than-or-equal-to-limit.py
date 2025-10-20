class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = collections.deque()
        min_dq = collections.deque()
        max_len = 0
        l = 0
        for r in range(len(nums)):
            while max_dq and max_dq[-1] < nums[r]:
                max_dq.pop()
            max_dq.append(nums[r])
            while min_dq and min_dq[-1] > nums[r]:
                min_dq.pop()
            min_dq.append(nums[r])
            while max_dq[0] - min_dq[0] > limit:
                if nums[l] == max_dq[0]:
                    max_dq.popleft()
                if nums[l] == min_dq[0]:
                    min_dq.popleft()
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len