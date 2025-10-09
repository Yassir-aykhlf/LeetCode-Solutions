class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res
        slow = n
        fast = n
        while True:
            slow = calc(slow)
            fast = calc(calc(fast))
            if fast == slow:
                return slow == 1