class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_words = defaultdict(list)
        for word in words:
            char_words[word[0]].append([word, 0])
        count = 0
        for c in s:
            group = char_words[c]
            char_words[c] = []
            for pair in group:
                word, index = pair
                index += 1
                if index == len(word):
                    count += 1
                else:
                    char_words[word[index]].append([word, index])
        return count