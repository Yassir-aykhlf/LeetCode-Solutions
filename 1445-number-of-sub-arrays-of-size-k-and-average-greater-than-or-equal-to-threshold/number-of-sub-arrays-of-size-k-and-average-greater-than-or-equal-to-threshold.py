class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        threshold_optimized = threshold * k
        count = 1 if window_sum >= threshold_optimized else 0
        for r in range(k, len(arr)):
            window_sum += arr[r]
            window_sum -= arr[r - k]
            if window_sum >= threshold_optimized:
                count += 1
        return count