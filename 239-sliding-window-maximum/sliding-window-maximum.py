class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        n = len(nums)
        for r in range(n):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            while dq and dq[0] <= r - k:
                dq.popleft() 
            dq.append(r)
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res