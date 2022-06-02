from src.email.email_queries import email_queries
from src.hostname.hostname_queries import host_queries
from src.ipv4.ipv4_queries import ip_queries
from src.threat_intel.threat_intel import intel_queries
from src.shared_functions import logger
import docs.conf as conf
import os


#Menu
os.system('cls')
run = True
print("#" * 120)
print("#" * 40 + " " * 8 + " Investigation Toolbox " + " " * 8 + "#" * 41)
while(run):
    print("#" * 120)
    print("1) Email Queries")
    print("2) IPv4 Queries")
    print("3) Hostname Queries")
    print("4) Threat Intelligence")
    print("5) Exit")
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
            email_rep_result = email_queries(user_email_input).email_rep()
            print(email_rep_result)
            continue
        if email_selector == "2":
            print(conf.result)
            email_breach_result = email_queries(user_email_input).breach_directory()
            print(email_breach_result)
            continue
        else:
            continue
    elif selector == "2":
        print()
        print("#" * 120)
        print("IPv4 Query Options")
        print("#" * 120)
        print("1) Abuse IPDB")
        ip_selector = input("Choose an option: ")
        user_ipv4_input = input("What is the IPv4 address?: ")
        if ip_selector == "1":
            print(conf.result)
            ipdb_ipv4_result = ip_queries(user_ipv4_input).abuse_ipdb()
            print(ipdb_ipv4_result)
            continue
        else:
            continue
    elif selector == "3":
        print()
        print("#" * 120)
        print("Hostname Query Options")
        print("#" * 120)
        print("1) Whois lookup")
        print("2) Shodan search")
        host_selector = input("Choose an option: ")
        user_host_input = input("What is the host name?: ")
        if host_selector == "1":
            print(conf.result)
            whois_result = host_queries(user_host_input).whois_lookup()
            print(whois_result)
            continue
        elif host_selector == "2":
            print(conf.result)
            shodan_result = host_queries(user_host_input).shodan_host()
            print(shodan_result)
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
            whois_result = host_queries(intel_input).whois_lookup()
            print(whois_result)
            continue
    elif selector == "5":
        break
    else:
        continue