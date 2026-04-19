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
                up = (int(code[i]) + 1) % 10
                up_code = code[:i] + str(up) + code[i+1:]
                if up_code not in deadSet:
                    deadSet.add(up_code)
                    dq.append((up_code, turns + 1))
                down = (int(code[i]) - 1) % 10
                down_code = code[:i] + str(down) + code[i+1:]
                if down_code not in deadSet:
                    deadSet.add(down_code)
                    dq.append((down_code, turns + 1))
        return -1