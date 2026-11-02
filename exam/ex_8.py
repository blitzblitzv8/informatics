#7
# from itertools import product
# count = 0
# for i in product('школа', repeat=3):
#     if i.count('к')==1:
#         count += 1
# print(count)
#31505
# from itertools import product
# c = 0
# s = 'а к ц е н т'.split()
# s.sort()
# for p in product(s, repeat=5):
#     c += 1
#     if p[0] not in ['а', 'е', 'к'] and p.count('т')>0 and c%2 == 0:
#         print(c, p)
#         break

#52
# from itertools import product
# count = 0
# for p in product('гафний', repeat=4):
#     if p[0] != 'й' and ('а' in p or 'и' in p):
#     # if p[0] != 'й' and (p.count('и')+p.count('а')>0):
#         count += 1
# print(count)

#17862
# from itertools import product
# a = '0123456789ab'
# count = 0
# for p in product(a, repeat = 5):
#     if p.count('7')==1 and sum([p.count(i) for i in '9ab'])<=3 and p[0] != '0':
#         count += 1
# print(count)

#9831 (50 - 56) - объясниение
# from itertools import permutations
# from string import printable
# a = '0123456789abcdef'
# count = 0
# for p in permutations(a, r=3):
#     if printable.index(p[0])%2 != printable.index(p[1])%2 and printable.index(p[1])%2 != printable.index(p[2])%2 and p[0]!='0':
#         count += 1
# print(count)
# from itertools import permutations
# a = '0123456789abcdef'
# count = 0
# bad = list(permutations('02468ace', r=2)) + list(permutations('13579bdf', r=2))
# for p in permutations(a, r=3):
#     if all(''.join(n) not in ''.join(p) for n in bad) and p[0]!='0':
#         count += 1
# print(count)

#6892
# from itertools import product
# a = '012345'
# count = 0
# bad = '12 32 52 21 23 25'.split()
# for p in product(a, repeat=6):
#     if p.count('2')==1 and p[0]!='0':
#         if all([i not in ''.join(p) for i in bad]):
#             count+=1
# print(count)

#6782
# from itertools import product
# a = '01234567'
# count = 0
# bad = '16 36 56 76 61 63 65 67'.split()
# for p in product(a, repeat=6):
#     if p.count('6')==2 and p[0]!='0':
#         if all([n not in ''.join(p) for n in bad]):
#             count += 1
# print(count)

#6894
# from itertools import product
# a = 'ц а п л я'.split()
# a.sort()
# count = 0
# for p in product(a, repeat=5):
#     count += 1
#     if p.count('а')<2 and p.count('ц')==2 and p.count('л')==0 and p[0]!='0':
#         print(count)
#         break

# Сколько существует восьмеричных пятизначных чисел,
# содержащих в своей записи ровно одну цифру 3, при этом
# никакая чётная цифра не стоит рядом с цифрой 3? В ответе
# запишите только число.
# from itertools import product
# a = '01234567'
# count = 0
# bad = '03 23 43 63 30 32 34 36'.split()
# for p in product(a, repeat=5):
#     if p.count('3')==1 and p[0]!='0':
#         if all([i not in ''.join(p) for i in bad]):
#             count+=1
# print(count)

# from itertools import product
#
# a = 'а д л о ш ь'.split()
# a.sort()
# c = 0
# for p in product(a, repeat=5):
#     c += 1
#     if p[0] != 'д' and p.count('ш') == 2 and p.count('о') == 0:
#         print(c)

from itertools import permutations
c=0
b = '13 33 53 73 93 b3 31 35 37 39 3b'.split()
for p in permutations('0123456789ab', r=4):
    if p[0]!='0'and len([i for i in b if i in ''.join(p)])==0:
        c+=1
print(c)
























