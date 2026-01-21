class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            domains[domain] += count
            for i, c in enumerate(domain):
                if c == '.':
                    dom = domain[i+1:]
                    domains[dom] += count
        return [f"{count} {dom}" for dom, count in domains.items()]