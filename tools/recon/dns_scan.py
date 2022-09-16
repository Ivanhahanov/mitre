import dns
import dns.resolver
import socket

domains = {}
subs = "subdomains.txt"

res = dns.resolver.Resolver()
res.nameservers = ["localhost"]
res.port = 8053

domain = "example.com"
nums = False
# res.nameservers = ["127.0.0.1"]
# res.port = 8053
# domain = "google.com"
# nums = False

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return []

def DNSRequest(domain):
    ips = []
    try:
        result = res.resolve(domain)
        if result:
            addresses = [a.to_text() for a in result]
            if domain in domains:
                domains[domain] = list(set(domains[domain]+addresses))
            else:
                domains[domain] = addresses
            for a in addresses:
                rd = ReverseDNS(a)
                for d in rd:
                    if d not in domains:
                        domains[d] = [a]
                        DNSRequest(d)
                    else:
                        domains[d] = [a]
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []
    return ips

def HostSearch(domain, dictionary,nums):
    successes = []
    for word in dictionary:
        d = word+"."+domain
        DNSRequest(d)
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)

dictionary = []
with open(subs,"r") as f:
    dictionary = f.read().splitlines()
HostSearch(domain,dictionary,nums)
for domain in domains:
    print("%s: %s" % (domain, domains[domain]))
