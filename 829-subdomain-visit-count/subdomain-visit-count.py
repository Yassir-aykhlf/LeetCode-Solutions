class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            domains[domain] += count
            for i, c in enumerate(domain):
                if c == ".":
                    domains[domain[i+1:]] += count
        return [f"{count} {domain}" for domain, count in domains.items()]