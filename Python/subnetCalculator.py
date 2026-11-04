#Created by Ethan Trombley

'''
This set up is to help easily create a subnet.
This will use the basic 192.168.x.x ip address string.

'''

import ipaddress

numOfHosts = int(input("How many hosts do you need? -> "))
amtOfSwitches = 0



def classC():

    ipv4 = ipaddress.ip_address("192.168.1.0")

    print("Class C network")
    n = 2
    while (2 ** n) - 2 < numOfHosts:
        n += 1

    blockSize = 2 ** n          # total addresses in the subnet
    usableHosts = blockSize - 2 # minus network + broadcast
    prefix = 32 - n

    print(f"Ip address: {ipv4 + usableHosts} Prefix: /{prefix}")    
    print(f"Bits used: {n}")
    print(f"Usable hosts: {usableHosts}")


def classB():

    ipv4 = ipaddress.ip_address("192.168.0.0")

    print("Class B network")
    n = 2
    while (2 ** n) - 2 < numOfHosts:
        n += 1

    blockSize = 2 ** n          # total addresses in the subnet
    usableHosts = blockSize - 2 # minus network + broadcast
    prefix = 32 - n

    print(f"Ip address: {ipv4 + usableHosts} Prefix: /{prefix}")
    print(f"Bits used: {n}")
    print(f"Usable hosts: {usableHosts}")

def classA():

    ipv4 = ipaddress.ip_address("192.0.0.0")

    print("Class A network")
    n = 2
    while (2 ** n) - 2 < numOfHosts:
        n += 1

    blockSize = 2 ** n          # total addresses in the subnet
    usableHosts = blockSize - 2 # minus network + broadcast
    prefix = 32 - n

    print(f"Ip address: {ipv4 + usableHosts} Prefix: /{prefix}")
    print(f"Bits used: {n}")
    print(f"Usable hosts: {usableHosts}")



if numOfHosts <= 250:
    classC()
elif numOfHosts > 250 and numOfHosts <= 65534:
    classB()
else:
    classA()



