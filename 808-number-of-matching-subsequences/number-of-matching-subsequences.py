class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        alpha = defaultdict(list)
        for word in words:
            alpha[word[0]].append([word, 0])
        for c in s:
            group = alpha[c]
            alpha[c] = []
            for pair in group:
                pair[1] += 1
                if len(pair[0]) == pair[1]:
                    count += 1
                else:
                    alpha[pair[0][pair[1]]].append(pair)
        return count