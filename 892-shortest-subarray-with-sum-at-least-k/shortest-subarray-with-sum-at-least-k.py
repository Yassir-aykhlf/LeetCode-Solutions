class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = collections.deque()
        
        for r in range(n + 1):

            while dq and prefix[r] - prefix[dq[0]] >= k:
                min_len = min(min_len, r - dq[0])
                dq.popleft()

            while dq and prefix[r] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(r)
            
        return min_len if min_len != float('inf') else -1