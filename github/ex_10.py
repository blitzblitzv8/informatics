#31507
# from ipaddress import ip_network
# net = ip_network('192.168.159.86/255.255.252.0', 0)
# for ip in net:
#     print(ip)
#     break

#29345
# from ipaddress import ip_network
# net = ip_network('68.203.243.87/255.255.224.0', 0)
# for ip in net:
#     print(ip)
# print(68+203+255+254)

#17867
# from ipaddress import ip_network
# net = ip_network('172.16.168.0/255.255.248.0', 0)
# ip = [i for i in net if f'{int(i):032b}'.count('1')%5!=0]
# print(len(ip))

#14650
# from ipaddress import ip_network
# for m in range(6, 31):#кол-во единичных бит в маске
#     net1 = ip_network(f'216.54.187.235/{m}', 0)
#     net2 = ip_network(f'216.54.174.128/{m}', 0)
#     ban1 = [str(net1[0]), str(net1[-1])]
#     ban2 = [str(net2[0]), str(net2[-1])]
#     if net1 != net2:
#         if '216.54.187.235' not in ban1:
#             if '216.54.174.128' not in ban2:
#                 print(m)

#10779
# from ipaddress import ip_network
# mask = 0
# for m in range(6, 30):
#     net1 = ip_network(f'201.92.0.20/{m}', 0)
#     net2 = ip_network(f'201.92.0.49/{m}', 0)
#     ban1= [str(net1[0]), str(net1[-1])]
#     ban2 = [str(net2[0]), str(net2[-1])]
#     if net1 == net2:
#         if '201.92.0.20' not in ban1:
#             if '201.92.0.49' not in ban1:
#                 mask = m
# net = ip_network(f'201.92.0.20/{mask}', 0)
# print(len(list(net))-4)
# from ipaddress import ip_network
# mask = 0
# for m in range(6, 30):
#     net1 = ip_network(f'201.92.0.20/{m}', 0)
#     net2 = ip_network(f'201.92.0.49/{m}', 0)
#     ban = [str(net1[0]), str(net1[-1])]
#     if net1 == net2:
#         if '201.92.0.20' not in ban and '201.92.0.49' not in ban:
#                 mask = m
# net = ip_network(f'201.92.0.20/{mask}', 0)
# print(len(list(net))-4)

#HOME_WORK
#10788
# count = 0
# from ipaddress import ip_network
# for m in range(5, 30):
#     net1 = ip_network(f'201.44.240.33/{m}', 0)
#     net2 = ip_network(f'201.44.240.107/{m}', 0)
#     ban = [str(net1[0]), str(net1[-1])]
#     if net1 == net2:
#         if '201.44.240.33' not in ban and '201.44.240.107' not in ban:
#             count +=1
# print(count)
# count = 0
# from ipaddress import ip_network
# for m in range(6, 30):
#     net1 = ip_network(f'201.44.240.33/{m}', 0)
#     net2 = ip_network(f'201.44.240.107/{m}', 0)
#     ban = [str(net1[0]), str(net1[-1])]
#     if net1 == net2:
#         if str(f'{int(net1[0]):032b}').count('1')>4:
#             count +=1
# print(count)

#25141
# from ipaddress import ip_network
# net = ip_network('46.29.170.214/255.255.128.0', 0)
# for ip in net:
#     print(ip)

#12922
# from ipaddress import ip_network
# net = ip_network('136.36.240.16/255.255.255.248', 0)
# count = 0
# for ip in net:
#     if str(f'{int(ip):032b}').count('101') == 0:
#         count += 1
# print(count)

#25352
# from ipaddress import ip_network
# net = ip_network('190.202.83.62/255.255.252.0', 0)
# for ip in net:
#     print(ip)
# print(190+202+83+254)

#18615
# from ipaddress import ip_network
# for m in range(10, 28):
#     count = 0
#     net = ip_network(f'143.131.211.37/{m}', 0)
#     for i in net:
#         if str(f'{int(i):032b}').count('1') == 10:
#             count += 1
#     if count == 15:
#         print(m)

#10785
# from ipaddress import ip_network
# for m in range(5, 28):
#     net = ip_network(f'192.75.64.98/{m}', 0)
#     if str(net[0]) == '192.75.64.0':
#         print(m)
#         break

#14948
# from ipaddress import ip_network
# net = ip_network('192.168.32.128/255.255.255.192', 0)
# count = 0
# for ip in net:
#     if str(f'{int(ip):023b}').count('1')%2 == 0:
#         count+=1
# print(count)

#10095
# from ipaddress import ip_network
# net = ip_network('192.168.32.160/255.255.255.240', 0)
# count = 0
# for ip in net:
#     if str(f'{int(ip):032b}').count('1')%2==0:
#         count += 1
# print(count)

#10172
# from ipaddress import ip_network
# count = 0
# for m in range(8, 30):
#     net = ip_network(f'175.122.80.13/{m}', 0)
#     if str(net[0]) == '175.122.80.0':
#         if len(list(net))>=60:
#             count += 1
# print(count)

#17709
# from ipaddress import ip_network
# net = ip_network('235.53.0.0/255.255.224.0', 0)
# count = 0
# for ip in net:
#     if str(f'{int(ip):032b}').count('1')%5 == 0 and str(f'{int(ip):032b}')[-3:]=='110':
#         count += 1
# print(count)

#14649
# def f(ip):
#     b = f'{int(ip):032b}'
#     return b[:16].count('1') >= b[16:].count('1')
# from ipaddress import ip_network
# for a in range(0, 256):
#     net = ip_network(f'116.242.{a}.26/255.255.255.224', 0)
#     if all([f(ip) for ip in net]):
#         print(a)

#HOME_WORK
#23272
# from ipaddress import ip_network
# net = ip_network('205.99.68.249/255.255.248.0', 0)
# print(net[-2])

#20902
# from ipaddress import ip_network
# net = ip_network('172.16.80.0/255.255.248.0', 0)
# c = 0
# for ip in net:
#     co=0
#     if (f'{int(ip):032b}').count('1')%2==1:
#         c+=1
# print(c)


#21739
# from ipaddress import ip_network
# net = ip_network('95.24.30.144/255.255.248.0', 0)
# print(net[1])
# print(95+24+24+1)

#21742
# from ipaddress import ip_network
# net = ip_network('95.24.20.25/255.255.252.0', 0)
# print(net.num_addresses-10-1-2)

#10779
# from ipaddress import ip_network
# for m in range(6, 30):
#     net1 = ip_network(f'201.92.0.20/{m}', 0)
#     net2 = ip_network(f'201.92.0.49/{m}', 0)
#     if net1==net2:
#         print(net1.num_addresses - 4)

#21745
# from ipaddress import ip_network
# max = 0
# for m in range(6, 31):
#     net1 = ip_network(f'95.24.2.9/{m}', 0)
#     net2 = ip_network(f'95.24.3.10/{m}', 0)
#     b1 = [str(net1[0]), str(net1[-1])]
#     b2 = [str(net2[0]), str(net2[-1])]
#     if net1 != net2 and '95.24.2.9' not in b1 and '95.24.3.10' not in b2:
#         count = 0
#         for ip in net1:
#             if f'{int(ip):032b}'[-1]=='0' and str(ip) not in b1:
#                 count+=1
#         if count>max:
#             max=count
#         count = 0
#         for ip in net2:
#             if f'{int(ip):032b}'[-1]=='0' and str(ip) not in b2:
#                 count+=1
#         if count>max:
#             max=count
# print(max)

# from ipaddress import *
# mx = 0
# for m in range(6, 31):
#     a = ip_network(f'95.24.2.9/{m}', 0)
#     b = ip_network(f'95.24.3.10/{m}', 0)
#     if a != b:
#         for net in (a, b):
#             mx = max(mx, net.num_addresses // 2 - 1)
# print(mx)


#10783
# from ipaddress import ip_network
# min = 1000000
# for m in range(6, 31):
#     net1 = ip_network(f'121.171.5.70/{m}', 0)
#     net2 = ip_network(f'121.171.5.107/{m}', 0)
#     if net1==net2:
#         c = net1.num_addresses
#         if min>c:
#             min = c
# print(min)

#10163
# from ipaddress import ip_network
# net = ip_network('192.168.156.235/255.255.255.240', 0)
# n=0
# for ip in net:
#     if str(ip)=='192.168.156.235':
#         print(n)
#     n+=1

#21740
# from ipaddress import ip_network
# net = ip_network('95.24.16.0/255.255.240.0', 0)
# c = []
# for i in net:
#     if i!= net[0] and i!=net[-1]:
#         c.append([(f'{int(i):032b}').count('1'), i])
# print(max(c))

#21744
# from ipaddress import ip_network
# min = 10000
# for m in range(10, 31):
#     net1 = ip_network(f'95.24.2.9/{m}', 0)
#     net2 = ip_network(f'95.24.3.10/{m}', 0)
#     if net1 == net2:
#         c = 0
#         for ip in net1:
#             if (f'{int(ip):032b}').count('0')%2==0:
#                 c+=1
#         if min>c:
#             min = c
# print(min)

#дуэлька
# from ipaddress import ip_network
# c=0
# for m in range(6, 31):
#     a = ip_network(f'182.101.181.99/{m}', 0)
#     if str(a[0])=='182.101.176.0':
#         c=m
#         break
# print(32-c)


























