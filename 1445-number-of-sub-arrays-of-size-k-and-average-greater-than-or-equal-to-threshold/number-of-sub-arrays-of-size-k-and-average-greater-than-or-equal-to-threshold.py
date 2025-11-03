class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        wsum = sum(arr[:k])
        count = 1 if (wsum / k >= threshold) else 0
        for r in range(k, len(arr)):
            wsum += arr[r]
            wsum -= arr[r - k]
            if wsum / k >= threshold:
                count += 1
        return count