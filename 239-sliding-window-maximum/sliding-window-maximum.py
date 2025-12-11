class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        res = []
        for r in range(n):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            while dq and dq[0] <= r - k:
                dq.popleft()
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res