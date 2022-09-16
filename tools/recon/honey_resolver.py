from dnslib import *
from dnslib.server import DNSServer

host="localhost"
port = 8053

subdomains = {
    "www.": "173.194.73.99",
    "smtp.": "64.233.162.27"
}
domain = "google.com"
honeyip = "10.0.0.0"

blocked = {}

class HoneyResolver:
    def resolve(self,request,handler):
        subdomain = str(request.q.qname.stripSuffix(domain+"."))
        if subdomain in subdomains:
            reply = request.reply()
            ip = subdomains[subdomain]
            reply.add_answer(RR(
                rname=request.q.qname,
                rtype=QTYPE.A,
                rclass=1,
                ttl=300,
                rdata=A(ip)))
        else:
            reply = request.reply()
            reply.add_answer(RR(
                rname=request.q.qname,
                rtype=QTYPE.A,
                rclass=1,
                ttl=300,
                rdata=A(honeyip)))
        return reply

resolver = HoneyResolver()
server = DNSServer(resolver,port=port,address=host)
server.start_thread()
while True:
    time.sleep(5)
server.stop()