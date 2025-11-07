class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = sum(arr[:k])
        count = 1 if cur_sum / k >= threshold else 0
        for r in range(k, len(arr)):
            cur_sum += arr[r]
            cur_sum -= arr[r - k]
            if cur_sum / k >= threshold:
                count += 1
        return count