class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            rep_str, domain = cpdomain.split()
            rep = int(rep_str)
            domain_count[domain] += rep
            for i, c in enumerate(domain):
                if c == '.':
                    sub_domain = domain[i+1:]
                    domain_count[sub_domain] += rep
        return [f"{rep} {domain}" for domain, rep in domain_count.items()]