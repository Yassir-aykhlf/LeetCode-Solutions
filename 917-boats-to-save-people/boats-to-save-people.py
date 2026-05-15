class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            wei = people[l] + people[r]
            if wei <= limit:
                l += 1
            r -= 1
            count += 1
        return count