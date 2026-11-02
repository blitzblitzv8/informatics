#31136
# from string import printable
#
# for x in printable[:23]:
#     x1 = int(f'81{x}9982', 23)
#     x2 = int(f'36{x}24', 23)
#     x3 = int(f'72{x}5', 23)
#     s = x1+x2+x3
#     if s%22 == 0:
#         print(x, s/22)
#         break

#28935
# from string import printable
# for x in printable[:23]:
#     x1 = int(f'761{x}035', 23)
#     x2 = int(f'338{x}932', 23)
#     if (x1+x2)%22==0:
#         print((x1+x2)//22)
#         break

#31152
# max = 0
# def seven(n):
#     N = ''
#     while n:
#         N = str(n%7)+N
#         n //=7
#     return N
# for x in range(1, 2031):
#     f = seven(7**170 + 7**100 - x)
#     if f.count('0')==70:
#         max = x
# print(max)

# for x in range(1, 2031):
#     f = 7**170 + 7**100 - x
#     count = 0
#     while f:
#         if f%7==0:
#             count += 1
#         f //= 7
#     if count == 70:
#         print(x)

#31121
# max = 0
# cx = 0
# for x in range(1, 2031):
#     f = 5**150 + 5**100 - x
#     count = 0
#     while f:
#         if f%5 == 0:
#             count+=1
#         f //= 5
#
#     if max<count or max == count:
#         max = count
#         cx = x
# print(cx)
# m = []
# for x in range(1, 2031):
#     f = 5**150 + 5**100 - x
#     count = 0
#     while f:
#         if f%5 == 0:
#             count+=1
#         f //= 5
#     m.append([count, x])
# print(max(m))

#29346
# f = 5 * 1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
# count = 0
# while f:
#     if f%36 % 2==0:
#         count += 1
#     f //= 36
# print(count)

#28760
# f = 2*2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561
# count = 0
# while f:
#     c = f%27
#     if c>9 and c%2==0:
#         count +=1
#     f //= 27
# print(count)

#27769
# from string import printable
# for x in printable[:22]:
#     f = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)
#     if f%21 == 0:
#         print(x, f//21)

#23935
# for x in range(18, 37):
#     f = int('22A12E', x) + int('2F1391', x) - int('1H05D0', x)
#     if f%19 == 0:
#         print(f/19)
#         break

#HOME_WORK
#27295
# min = 1000
# for x in range(1, 32000):
#     f = 75**314 + 75**118 - x
#     count = 0
#     while f:
#         if f%75 == 0:
#             count +=1
#         f //= 75
#     if count<min:
#         min = count
# print(min)

#4702
# from string import printable
# for x in printable[:15]:
#     f = int(f'123{x}5', 15) + int(f'1{x}233', 15)
#     if f%14==0:
#         print(x, f//14)
#         break

#29346
# f = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
# count = 0
# while f:
#     if f%36%2==0:
#         count +=1
#     f //= 36
# print(count)

#23273
# from string import printable
# for x in printable[:29]:
#     f = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
#     if f%28==0:
#         print(f//28)
#         break

#17868
# from string import printable
# for x in printable[:19]:
#     f = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#     if f%18==0:
#         print(f/18)

#25353
# for x in range(1, 27000):
#     f = 3*27**9 + 2*27**6 + 27**3 - x
#     count=0
#     while f:
#         if f%27 == 0:
#             count += 1
#         f //= 27
#     if count == 6:
#         print(x)
#         break

#8502
# from string import printable
# for x in printable[:15]:
#     f = int(f'99658{x}29', 15) + int(f'102{x}023', 15)
#     if f%14 == 0:
#         print(f/14)

#5952
# from string import printable
# for x in printable[:16]:
#     f = int(f'10{x}a', 16) + int(f'ff{x}78', 16)
#     if f%19 == 0:
#         print(f/19)
#         break

#11305
# from string import printable
# for x in printable[:29]:
#     f = int(f'47{x}42696', 29) + int(f'8{x}22', 29)
#     if f%28 == 0:
#         print(f/28)

#8597
# c=0
# from string import printable
# for x in printable[:15]:
#     f = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
#     if f%11 == 0:
#         c += printable.index(x)
# print(c)

f = 2*25**374 + 3*25**317 + 25**298 - 1963
count = 0
while f:
    if f%25==0:
        count+=1
    f//=25

print(count)