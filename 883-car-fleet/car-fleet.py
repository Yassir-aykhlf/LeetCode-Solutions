class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            t = (target - p) / s
            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)