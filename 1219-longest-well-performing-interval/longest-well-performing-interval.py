class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_len = 0
        curr_sum = 0
        sum_to_index = {0: -1}
        for i, h in enumerate(hours):
            curr_sum += 1 if h > 8 else -1
            if curr_sum > 0:
                max_len = i + 1
            else:
                if curr_sum - 1 in sum_to_index:
                    max_len = max(max_len, i - sum_to_index[curr_sum - 1])
            if curr_sum not in sum_to_index:
                sum_to_index[curr_sum] = i
        return max_len