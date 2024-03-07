import scapy.all as scapy
from scapy.all import conf
from os import system as s


def cls():
    s("cls")


def ph():
    return "Sorry, this tool is currently indev"


def get_user_input():
    user_input = input("Enter IP: ")
    return user_input


def scan_my_network(ip):
    try:
        arp_request_packet = scapy.ARP(pdst=ip)
        combined_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / arp_request_packet
        answered_list = scapy.srp(combined_packet, timeout=1, iface=conf.L3socket(), verbose=False)[0]
    except Exception as f:
        print(f"""Something went wrong :(
        Please Try Again!
        Error Code: {f}""")
        return

    answered_list.summary()


def main():
    cls()
    while True:
        print("""WARNING: This code might not work on some computers and REQUIRES Winpcap(not wincap).
            If not working try running Games n' Tools with administrator privilages""")
        print("""Welcome to the net scanner! Please keep in mind that this code is pretty unstable!
        R - Run Scanner
        Q - Quit""")
        c = input("Choice: ")
        if c.lower() == "r":
            user_ip_address = get_user_input()
            scan_my_network(user_ip_address)
        elif c.lower() == "q":
            break
        else:
            print("Unknown choice. Try again")
            cls()
