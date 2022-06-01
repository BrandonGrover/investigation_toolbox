import modules
import os
import config
result = "#" * 120 + "\n" + "#" * 48 + " " * 8 + " Result " + " " * 8 + "#" * 48 + "\n" + "#" * 120
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
    print("4) Exit")
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
            print(result)
            email_rep_result = modules.email_queries(user_email_input).email_rep()
            print(email_rep_result)
            continue
        if email_selector == "2":
            print(result)
            email_breach_result = modules.email_queries(user_email_input).breach_directory()
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
            print(result)
            ipdb_ipv4_result = modules.ip_queries(user_ipv4_input).abuse_ipdb()
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
        host_selector = input("Choose an option: ")
        user_host_input = input("What is the domain name?: ")
        if host_selector == "1":
            print(result)
            whois_result = modules.host_queries(user_host_input).whois_lookup()
            print(whois_result)
            continue
        else:
            continue
    elif selector == "4":
        break
    else:
        continue