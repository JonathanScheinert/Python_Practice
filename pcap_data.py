
#Jonatan Scheinert

#Question 1
import re
proto_list = []
proto_dict = {}
freq_dict = {}
with open('net.log','r') as file:
	for line in file:
		words = line.split()
		if ':' in line:
			continue
		proto_dict[words[2]] = proto_dict.get(words[2], 0) +1
print("How many protocols?")
print(len(proto_dict))
print(list(proto_dict.items())[0] , "Most frequently used protocol: TCP")
print(list(proto_dict.items())[14], "east frequently used protocol: RTCP")

#Question 2

import re
ip_list = []
ip_dict = {}
freq_dict = {}
with open('net.log','r') as file:
	for line in file:
		words = line.split()
		if ':' in line:
			continue
		ip_dict[words[3]] = ip_dict.get(words[3], 0) +1
		ip_dict[words[4]] = ip_dict.get(words[4], 0) +1
	
#How many different IP addresses did you find? 438
count_1000 = 0
for v in ip_dict:
	if ip_dict[v] > 1000:
		count_1000 += 1
print("different IP addresses:",len(ip_dict))
print("IP addresses appear more than a 1,000:", count_1000)

#How many IP addresses appear more than a 1,000 times? 23
#Can you print these IP addresses? in the code above.

#Question 3

import re
ip_dict = {}
prv_ip = []
multi_ip = []
public_ip = []
with open('net.log','r') as file:
	for line in file:
		words = line.split()
		if ':' in line:
			continue
		ip_dict[words[3]] = ip_dict.get(words[3], 0) +1
		ip_dict[words[4]] = ip_dict.get(words[4], 0) +1
for k,v in ip_dict.items():
	if k.startswith("127."):
		prv_ip.append(k)
	elif k.startswith("10."):
		prv_ip.append(k)
	elif k.startswith("192.168."):
		prv_ip.append(k)
	elif k.startswith("224."):
		multi_ip.append(k)
		x = k.split(".")
		if int(x[0]) >= 224 and int(x[0]) <= 239:
			multi_ip.append(k)
	elif k.startswith("172."):
		x = k.split(".")
		if int(x[1]) >= 16 and int(x[1]) <= 31:
			prv_ip.append(k)
	else:
		public_ip.append(k)
print("uniq private ip's:",len(prv_ip),"\nuniq multicast ip's:",len(multi_ip),"\nuniq public ip's:",len(public_ip),"\nmore frequent: public ip's")

#What type of address is more frequent? Private, Public or Multicast addresses? 


