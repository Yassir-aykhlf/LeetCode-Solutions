class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        c = Counter()
        for i in range(n):
            c[senders[i]] += messages[i].count(' ') + 1
        return sorted(c.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]