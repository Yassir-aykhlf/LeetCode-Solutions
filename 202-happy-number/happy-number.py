class Solution:
    def isHappy(self, n: int) -> bool:
        def mutate(n):
            res = 0
            while n:
                res += (n % 10) * (n % 10)
                n //= 10
            return res
        slow = n
        fast = n
        while True:
            slow = mutate(slow)
            fast = mutate(mutate(fast))
            if slow == fast:
                return slow == 1