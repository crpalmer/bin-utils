#!/usr/bin/python

import socket
import os
from cloudflare import Cloudflare
from unifi_controller_api import UnifiController

def get_zone(domain):
    for zone in client.zones.list():
        if zone.name == domain:
            return zone

def get_dns_records(zone):
     return client.dns.records.list(zone_id=zone.id)

def get_dns_record(dns_records, full_hostname, type):
    for dns_record in dns_records:
        if dns_record.name == full_hostname and dns_record.type == type:
            return dns_record

def create_dns_record(zone, full_hostname, type, ip):
    print("Creating " + full_hostname + " @ " + ip)
    client.dns.records.create(
                zone_id = zone.id,
                name = full_hostname,
                ttl = 3600,
                content = ip,
                type = type 
           )

def create_or_update_dns_record(zone, dns_records, full_hostname, type, ip):
    dns_record = get_dns_record(dns_records, full_hostname, type)
    if dns_record is None:
        create_dns_record(zone, full_hostname, type, ip)
    elif dns_record.content == ip:
        print("DNS record unchanged for " + full_hostname + " @ " + ip + "[" + type + "]")
    else:
        print("Updating " + full_hostname + " changed from " + dns_record.content + " to " + ip)
        dns_record.content = ip
        client.dns.records.edit(
            dns_record_id = dns_record.id,
            zone_id = zone.id,
            content = ip,
            type = type,
            ttl = 3600,
            name = full_hostname
        )

domain='crpalmer.net'

# import logging
# logging.getLogger("unifi_controller_api").setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG) # Example: Show INFO level and above

controller = UnifiController(
    controller_url="https://unifi.crpalmer.net:11443", # Use :443 for UniFi OS, :8443 for legacy
    username="admin",
    password="AdminPassword1!",
    is_udm_pro=True, # Set True for UniFi OS devices (UDM, Cloud Key Gen2+), False for legacy software/hardware controllers
    verify_ssl=False, # Or path to your CA bundle, set True if using a valid public certificate
    auto_model_mapping=True, # Optional: Attempt to map device model codes to friendly names
    model_db_path=None, # Optional: Path to a custom model database file
    auth_retry_enabled=False, # Optional: Enable automatic retries on authentication failure
    auth_retry_count=3, # Optional: Number of authentication retries
    auth_retry_delay=5 # Optional: Delay in seconds between authentication retries
)

print("Unifi: Logged in, attempting to retrieve the sites")

devices = controller.get_unifi_site_client(site_name="0it6q3bo")

print("Logging in to cloudflare")

with open("/home/crpalmer/.cloudflare.key", "r", encoding="utf-8") as file:
    api_token = str.strip(file.read())

client = Cloudflare(api_token=api_token)

print("Getting DNS data")
zone = get_zone(domain)
dns_records = get_dns_records(zone)

print("Verifying IP addresses")
for device in devices:
    if "hostname" in device and "use_fixedip" in device and device["use_fixedip"]:
        full_hostname = str.lower(device["hostname"] + "." + domain)
        ip = None
        ipv6 = None
        if "ip" in device:
            ip = device["ip"]
        elif "last_ip" in device:
            ip = device["last_ip"]
        if "ipv6_addresses" in device:
            ipv6 = device["ipv6_addresses"][0]
        elif "last_ipv6" in device:
            ipv6 = device["last_ipv6"][0]

        if ip is not None:
            create_or_update_dns_record(zone, dns_records, full_hostname, "A", ip)
        if ipv6 is not None:
            create_or_update_dns_record(zone, dns_records, full_hostname, "AAAA", ipv6)
