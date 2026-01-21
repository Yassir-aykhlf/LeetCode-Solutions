class Solution:
    def isHappy(self, n: int) -> bool:
        def mutate(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res
        slow = fast = n
        while True:
            slow = mutate(slow)
            fast = mutate(mutate(fast))
            if slow == fast:
                slow = n
                while slow != fast:
                    slow = mutate(slow)
                    fast = mutate(fast)
                return slow == 1