class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        arr_slice = arr[:k]
        wsum = sum(arr_slice)
        if wsum / k >= threshold:
            count += 1
        for r in range(k, n):
            wsum += arr[r]
            wsum -= arr[r - k]
            if wsum / k >= threshold:
                count += 1
        return count