class Solution:
    def isHappy(self, n: int) -> bool:
        def mutate(num):
            res = 0
            while num > 0:
                res += (num % 10) * (num % 10)
                num //= 10
            return res
        slow = fast = n
        while True:
            slow = mutate(slow)
            fast = mutate(mutate(fast))
            if slow == fast:
                return slow == 1