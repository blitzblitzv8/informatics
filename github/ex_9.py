#31355
# в строке только одно число повторяется трижды, остальные числа различны;
# куб повторяющегося числа строки меньше произведения всех её неповторяющихся чисел.
# count = 0
# for line in open('text.txt'):
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i) == 3]
#     np = [i for i in a if a.count(i) == 1]
#     if len(p3) == 3 and len(np) == 3:
#         if p3[0]**3 < np[0]*np[1]*np[2]:
#             count += 1
# print(count)

# 31506
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i) == 1]
#     new = [i for i in a if i!= max(a) and i != min(a)]
#     if len(np) == 5 and (new[0] + new[1] + new[2]) < (2*(min(a) + max(a))):
#         count +=1
# print(count)

#23268
# count = 0
# for line in open('text'):
#     count += 1
#     a = [int(i) for i in line.split()]
#     p2 = [i for i in a if a.count(i) == 2]
#     np = [i for i in a if a.count(i) == 1]
#     if len(p2) == 4 and len(np) == 3:
#         if sum(p2)/3 < max(np):
#             print(count)
#             break

#19481
# count = 0
# nomer = 0
# for line in open('text'):
#     nomer += 1
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i) == 1]
#     # np.sort()
#     # if len(np) == 4 and (np[0] + np[-1])**2 > np[1]**3 + np[2]**3:
#     #     count += nomer
#     new = [i for i in a if i != min(a) and i != max(a)]
#     if len(np) == 4 and (min(a) + max(a))**2 > new[0]**3 + new[1]**3:
#         count += nomer
# print(count)

#24347
# count = 0
# for line in open('text'):
#     c = 0
#     a = [int(i) for i in line.split()]
#     b = sorted(a)
#     m = [min(a), max(a)]
#     u1 = a.count(max(a)) == 1
#     #u2 =  a[0] != max(a) and a[0] != min(a) and a[-1] != max(a) and a[-1] != min(a)
#     u2 = a[0] not in m and a[-1] not in m
#     u3 = (b[-1]*b[-2]*b[-3])%b[0] == 0
#     if u1 + u2 + u3 == 1:
#         count+=1
# print(count)

#HOME_WORK
#9740
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i) == 3]
#     np = [i for i in a if a.count(i) == 1]
#     if len(p3) == 3 and len(np) == 4:
#         if sum(np)/4 <= p3[0]:
#             count +=1
# print(count)

#19481
# count = 0
# nomer = 0
# for line in open('text'):
#     nomer +=1
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i) == 1]
#     a.sort()
#     if len(np) == 4 and (a[0] + a[-1])**2 > a[1]**3 + a[2]**3:
#         count += nomer
# print(count)

#18594
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     a.sort()
#     n = [i for i in a if i%2 == 0]
#     if len(n) == 2 and a[0]**2 <= sum(a)-a[0]:
#         count += 1
# print(count)

#9539
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p2 = [i for i in a if a.count(i) == 2]
#     p2.sort()
#     p1 = [i for i in a if a.count(i) == 1]
#     if len(p2) == 4 and p2[0] < p1[0] < p2[-1]:
#         count +=1
# print(count)

#31355
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i)==3]
#     np = [i for i in a if a.count(i)==1]
#     if len(np) == 3:
#         if len(p3) == 3 and p3[0]**3 < np[0]*np[1]*np[2]:
#             count +=1
# print(count)

#27764
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i) == 1]
#     np.sort()
#     if len(np) == 5 and 2*(np[0] + np[-1]) == (np[1]+np[2]+np[3]):
#         count+=1
# print(count)

#27287
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i)==3]
#     np = [i for i in a if a.count(i)==1]
#     p3.sort()
#     if len(p3)==6:
#         if np[0]<=p3[0]:
#             print(p3[-1])
#             break

#27285
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     ch = [i for i in a if i%2==0]
#     b = sorted(a, reverse=True)
#     if a != b and len(ch)>=4:
#         count+=1
# print(count)

#27284
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i)==1]
#     np.sort()
#     if (a.count(min(a)) == 2 or a.count(min(a)) == 3) and (len(np) == 5 or len(np) == 4):
#         if np[0]+np[-1]>sum(np)-(np[0]+np[-1]):
#             count+=1
# print(count)

#6925
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p2 = [i for i in a if a.count(i)==2]
#     np = [i for i in a if a.count(i)==1]
#     ch = [i for i in a if i%2 == 0]
#     nch = [i for i in a if i % 2 == 1]
#     u1 = len(p2) == 2 and len(np) == 4
#     if len(ch) == 0 or len(nch) == 0:
#         u2 = sum(ch)/6 + sum(nch)/6 > 50
#     else:
#         #u2 = (sum(ch)/len(ch) + 50 > sum(nch)/len(nch)) or (sum(nch)/len(nch) - 50 < sum(ch)/len(ch))
#         u2 = abs(sum(ch)/len(ch) - sum(nch)/len(nch)) > 50
#     if u1+u2 == 1:
#         count += 1
# print(count)

#5946
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a.count(i)==1]
#     ch = [i for i in a if i%2==0]
#     if len(np)==6 and len(ch)>3:
#         count += 1
# print(count)

#4635
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p = [i for i in a if a.count(i)>1]
#     a.sort()
#
#     if (a[0]**2)*2 > a[1]*a[2] and len(p) > 1 and a[2] != a[3]:
#         count += 1
# print(count)

#19241
# nomer = 0
# max = 0
# for line in open('text'):
#     nomer+=1
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i) == 3]
#     if len(p3)==6 and sum(p3)/6 < sum(a)-sum(p3):
#         max = nomer
# print(max)

#4259
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     a.sort()
#     if (a[0]+a[-1])**3 > a[1]**3 + a[2]**3 + a[3]**3:
#         count+=1
# print(count)

#8153
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     np = [i for i in a if a. count(i) == 1]
#     a.sort()
#     if len(np)==5 and a[0]+a[-1] < a[1]+a[2]+a[3]:
#
#         count += 1
# print(count)

#29962
# nomer = 0
# max = 0
# for line in open('text'):
#     nomer+=1
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i)==3]
#     np = [i for i in a if a.count(i)==1]
#     if len(p3)==3 and len(np)==4 and sum(np)/4>p3[0]:
#         max = nomer
# print(max)

#6357
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     p = [i for i in a if a.count(i)>1]
#     n = [i for i in a if a.count(i)==1]
#     if len(p)>0 and len(n)>0 and sum(n)/len(n)<sum(p)/len(p):
#         count+=1
# print(count)

#12726
# nomer = 0
# max=0
# for line in open('text'):
#     nomer+=1
#     a = [int(i) for i in line.split()]
#     p3 = [i for i in a if a.count(i)==3]
#     n = [i for i in a if a.count(i)==1]
#     ch = [i for i in a if i%2==0]
#     if len(p3)==3 and len(n)==4 and len(ch)>3:
#         max = nomer
# print(max)

#17770 (7 мин)
# count = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     a.sort()
#     n = [i for i in a if str(i)[-1] == '5']
#     if 2*(a[-1]+a[-2])>3*(a[0]+a[1]+a[2]) and len(n)>1:
#         count+=1
# print(count)

#16256 (55)

# max = 0
# for line in open('text'):
#     a = [int(i) for i in line.split()]
#     a.sort()
#     at = set(a)
#     if len(at) == 2:
#         if sum(a) - 2 * sum(at) > len(set(a)):
#             max = sum(a)
# print(max)


#самая частая ошибка: забывала, что при проверке длины списка нужно ставить len
#столкнулась с отвратительной для меня формулировкой "расположенные в порядке неубывания"

#4259
count = 0
for line in open('../text'):
    a = [int(i) for i in line.split()]
    a.sort()
    if (a[0]+a[-1])**3 > a[1]**3 + a[2]**3 +a[3]**3:
        count += 1
print(count)

















