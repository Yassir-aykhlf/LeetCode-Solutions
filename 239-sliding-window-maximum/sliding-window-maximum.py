class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res  = []
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            while dq and dq[0] <= r - k:
                dq.popleft()
            dq.append(r)
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res