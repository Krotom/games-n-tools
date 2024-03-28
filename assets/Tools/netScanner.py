import scapy.all as scapy
from os import system as s


def cls():
    s("cls")


def ph():
    return "Sorry, this tool is currently indev"


def get_user_input():
    verbo = True
    user_input = input("Enter IP: ")
    cf = input("Verbose? Y/n: ")
    if cf.lower() == "n":
        verbo = False
    return user_input, verbo


def scan_my_network(ip, verbose):
    try:
        arp_request_packet = scapy.ARP(pdst=ip)
        combined_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / arp_request_packet
        answered_list = scapy.srp(combined_packet, timeout=1, verbose=verbose)[0]
        print(answered_list.summary())
        print("Emmission finished, send again?")
        v = input("+/-:")
        if v == "+":
            scan_my_network(ip, verbose)
    except Exception as f:
        print(f"""Something went wrong :(
        Please Try Again!
        Error Code: {f}""")
        return


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
            print("Currently scannable addresses:")
            s("arp -a")
            user_ip_address, verb = get_user_input()
            scan_my_network(user_ip_address, verb)
        elif c.lower() == "q":
            break
        else:
            cls()
            print("Unknown choice. Try again")
