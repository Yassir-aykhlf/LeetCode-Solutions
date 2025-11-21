class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        doms = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            doms[domain] += count
            for i, c in enumerate(domain):
                if c == '.':
                    doms[domain[i+1:]] += count
        return [f"{count} {domain}" for domain, count in doms.items()]