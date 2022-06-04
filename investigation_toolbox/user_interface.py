from src.email.email_queries import email_queries
from src.hostname.hostname_queries import host_queries
from src.ipv4.ipv4_queries import ip_queries
from src.threat_intel.threat_intel import intel_queries
from src.scan.scan_queries import scan_queries
from src.modules.shodan import *
from src.shared_functions import logger
import docs.conf as conf
import os

#print(shodan(ipv4="45.223.18.234").shodan_scan())
print(shodan().scan_status(id_='rnmUMG9VTeRotZ28'))
#Menu
#os.system('cls')
run = False
if run:
    print("#" * 120)
    print("#" * 40 + " " * 8 + " Investigation Toolbox " + " " * 8 + "#" * 41)
    print("#" * 120)
while(run):
    print("1) Email Queries")
    print("2) IPv4 Queries")
    print("3) Hostname Queries")
    print("4) Threat Intelligence")
    print("5) Scanning")
    print("6) Exit")
    print("#" * 120)
    selector = input("Choose an option: ")
    if selector == "1":
        print()
        print("#" * 120)
        print("Email Query Options")
        print("#" * 120)
        print("1) Email Reputation")
        print("2) Email Breach Sources")
        email_selector = input("Choose an option: ")
        user_email_input = input("What is the email address?: ")
        if email_selector == "1":
            print(conf.result)
            email_result = email_queries(user_email_input).email_rep()
            print(email_result)
            continue
        if email_selector == "2":
            print(conf.result)
            email_result = email_queries(user_email_input).breach_directory()
            print(email_result)
            continue
        else:
            continue
    elif selector == "2":
        print()
        print("#" * 120)
        print("IPv4 Query Options")
        print("#" * 120)
        print("1) Abuse IPDB")
        print("2) Shodan Search")
        ip_selector = input("Choose an option: ")
        user_ipv4_input = input("What is the IPv4 address?: ")
        if ip_selector == "1":
            print(conf.result)
            ip_result = ip_queries(user_ipv4_input).abuse_ipdb()
            print(ip_result)
            continue
        if ip_selector == "2":
            print(conf.result)
            ip_result = ip_queries(user_ipv4_input).shodan_ipv4()
            print(ip_result)
        else:
            continue
    elif selector == "3":
        print()
        print("#" * 120)
        print("Hostname Query Options")
        print("#" * 120)
        print("1) Whois Lookup")
        print("2) Shodan Search")
        host_selector = input("Choose an option: ")
        user_host_input = input("What is the host name?: ")
        if host_selector == "1":
            print(conf.result)
            hostname_result = host_queries(user_host_input).whois_lookup()
            print(hostname_result)
            continue
        elif host_selector == "2":
            print(conf.result)
            hostname_result = host_queries(user_host_input).shodan_host()
            print(hostname_result)
            continue
        else:
            continue
    elif selector == "4":
        print()
        print("#" * 120)
        print("Threat Intelligence Options")
        print("#" * 120)
        print("1) Threat Miner")
        intel_selector = input("Choose an option: ")
        intel_input = input("What would you like to look up?: ")
        if intel_selector == "1":
            print(conf.result)
            intel_response = host_queries(intel_input).whois_lookup()
            print(intel_response)
            continue
    elif selector == "5":
        print()
        print("#" * 120)
        print("Scanning Options")
        print("#" * 120)
        print("1) On-Demand Shodan IP Scanning")
        print("2) Shodan Scan List")
        scan_selector = input("Choose an option: ")
        if not scan_selector == "2":
            scan_input = input("What IP would you like to look up?: ")
        if scan_selector == "1":
            print(conf.result)
            scan_response = scan_queries(scan_input).shodan_scan()
            print(scan_response)
            continue
        if scan_selector == "2":
            print(conf.result)
            scan_response = scan_queries().shodan_list()
            print(scan_response)
            continue
    elif selector == "6":
        break
    else:
        continue