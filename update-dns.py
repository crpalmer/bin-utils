#!/usr/bin/python

import socket
import os
from cloudflare import Cloudflare

client = Cloudflare(
    api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),  # This is the default and can be omitted
)

domain='crpalmer.org'

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('2001:4860:4860::8888', 1))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

full_hostname = get_hostname() + '.' + domain
ip = get_local_ip()
for zone in client.zones.list():
    if zone.name == domain:
        dns_records = client.dns.records.list(zone_id=zone.id)
        for dns_record in dns_records:
            if dns_record.name == full_hostname:
                if dns_record.content == ip:
                    print("DNS record unchanged for " + full_hostname + " @ " + ip)
                else:
                    print("Updating " + full_hostname + " changed from " + dns_record.content + " to " + ip)
                    dns_record.content = ip
                    client.dns.records.edit(
                        dns_record_id = dns_record.id,
                        zone_id = zone.id,
                        content = ip,
                        type = "AAAA",
                        ttl = 3600,
                        name = full_hostname
                    )
                exit()

        print("Creating " + full_hostname + " @ " + ip)
        client.dns.records.create(
                    zone_id = zone.id,
                    name = full_hostname,
                    ttl = 3600,
                    content = get_local_ip(),
                    type = "AAAA"
               )
        exit()
