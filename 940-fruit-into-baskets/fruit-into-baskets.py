class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = collections.defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(fruits)):
            baskets[fruits[r]] += 1
            while len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len