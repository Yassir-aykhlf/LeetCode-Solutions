class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        doc = defaultdict(int)
        for cpdomain in cpdomains:
            count_domain = cpdomain.split()
            sub_domains = count_domain[1].split('.')
            for i in range(len(sub_domains)):
                domain = '.'.join(sub_domains[i:],)
                doc[domain] += int(count_domain[0])
        return [f"{count} {dom}" for dom, count in doc.items()]