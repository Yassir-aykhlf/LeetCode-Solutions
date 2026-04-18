class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet = set(deadends)
        if "0000" in deadSet:
            return -1
        dq = deque([("0000", 0)])
        deadSet.add("0000")
        while dq:
            code, turns = dq.popleft()
            if code == target:
                return turns
            for i in range(4):
                up_digit = (int(code[i]) + 1) % 10
                perm = code[:i] + str(up_digit) + code[i+1:]
                if perm not in deadSet:
                    deadSet.add(perm)
                    dq.append((perm, turns + 1))
                down_digit = (int(code[i]) - 1) % 10
                perm = code[:i] + str(down_digit) + code[i+1:]
                if perm not in deadSet:
                    deadSet.add(perm)
                    dq.append((perm, turns + 1))
        return -1