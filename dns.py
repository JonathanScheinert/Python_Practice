from scapy.all import *
from netaddr import *
import socket
import sys

def checkdns(pkt):
	try:
		reply=pkt[1]
		ip=reply[DNSRR].rdata
		if valid_ipv4(ip):
			return True
	except:
		return False
valid=[]
invalid=[]
def request(listservers, domain):
	ans,unans = sr(IP(dst=listservers)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain)), verbose=0,timeout=1)
	for pkt in ans:
		if checkdns(pkt):
			valid.append(pkt[1][IP].src)
		else:
			invalid.append(pkt[1][IP].src)
		for pkt in unans:
			invalid.append(pkt[0][IP].dst)	
	return vaild,invalid


	# if checkdns(ansdns):
	# 	return True
	# else:
	# 	return False

	
invalid=[]
valid=[]
ipv4list=[]

with open('dns.txt','r') as file:
	for line in file:
		line =line.replace('\n','')
		line =line.replace(' ', '')
		if valid_ipv4(line):
			ipv4list.append(line)

ipv4list = list(set(ipv4list))
print(ipv4list)
#calling the function of determinaing ips is a real server 
validnds, invaliddns = request(ipv4list,'www.google.com')
print(len(validdns))




