from scapy.all import *
import ipaddress
from random import randint
ports = [53, 80, 8080, 8443]


def SynScan(host):
    ans, unans = sr(
        IP(dst=host) / TCP(sport=randint(10000, 65532), dport=ports, flags="S"), timeout=2, verbose=1
    )
    print("Open ports at %s:" % host)
    for s, r in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags == "SA":
            print(s[TCP].dport)


def DNSScan(host):
    ans, unans = sr(
        IP(dst=host) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="google.com")),
        timeout=2,
        verbose=0,
    )
    if ans and ans[UDP]:
        print("DNS Server at %s" % host)


host = sys.argv[1]
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)
SynScan(host)
DNSScan(host)
