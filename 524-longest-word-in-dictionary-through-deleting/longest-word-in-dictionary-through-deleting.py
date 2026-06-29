class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        word_to_freq = defaultdict(int)
        def score(word):
            i, j = 0, 0
            count = 0
            while i < len(s) and j < len(word):
                if word[j] == s[i]:
                    count += 1
                    j += 1
                i += 1
            return count if count == len(word) else -1
        for w in dictionary:
            word_to_freq[w] = score(w)
        sol = sorted(word_to_freq.items(), key=lambda x: (-x[1], x[0]))[0]
        return sol[0] if sol[1] and sol[1] != -1 else ""