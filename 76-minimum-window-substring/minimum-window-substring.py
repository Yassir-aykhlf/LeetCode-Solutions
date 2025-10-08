class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        """
        *   state variables: 
                target  => the frequencies of chars in the pattern
                state   => the current frequency of the window
                found   => the number of characters that are compatible with pattern
                missing => the number of characters that are yet to find
                count   => the lenght of the current window
        """
        target = collections.Counter(t)
        state = collections.defaultdict(int)
        found, missing = 0, len(target)
        count = float('inf')
        result = ""
        l = 0
        for r in range(n):
            state[s[r]] += 1
            if s[r] in target and target[s[r]] == state[s[r]]:
                found += 1
            # the shrinking; when all conditions are met, we keep shrinking to meet the smallest possible answer
            while found == missing:
                # update the result and count when I get a better result
                if r - l + 1 < count:
                    count = r - l + 1
                    result = s[l:r+1]
                if s[l] in target and target[s[l]] == state[s[l]]:
                    found -= 1
                state[s[l]] -= 1
                l += 1
        return result