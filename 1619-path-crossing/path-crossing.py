class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locs = set()
        locs.add((0, 0))
        start = [0, 0]
        for d in path:
            if d == "N":
                start[0] += 1
            elif d == "S":
                start[0] -= 1
            elif d == "E":
                start[1] += 1
            elif d == "W":
                start[1] -= 1
            if tuple(start) in locs:
                return True
            locs.add(tuple(start))
        return False