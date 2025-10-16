class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        window = collections.defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len