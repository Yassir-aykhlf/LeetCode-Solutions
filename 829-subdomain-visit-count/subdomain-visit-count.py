class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        group = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            group[domain] += count
            for i, c in enumerate(domain):
                if c == '.':
                    group[domain[i+1:]] += count
        return [f"{count} {domain}" for domain, count in group.items()]