class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0
        fruit_count = collections.defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            fruit_count[fruits[r]] += 1
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l += 1
            max_count = max(max_count, r - l + 1)
        return max_count