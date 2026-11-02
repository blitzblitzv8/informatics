#1958
# def f(N):
#     b = bin(N) [2:]
#     b += str((b.count('1') % 2))
#     b = b + str((b.count('1') % 2))
#     r = int(b, 2)
#     return r
# for i in range(1, 100):
#     if f(i) > 77:
#         print(i, f(i))
#         break
# #через генератор списков
# print(min(N for N in range(1, 100) if f(N)>77))
#1849
# def f(N):
#     b = bin(N)[2:]
#     if N % 2 == 0:
#         b = '1' + b + '0'
#     else: b = '11' + b + '11'
#     return int(b, 2)
# print(min(f(N) for N in range(1, 1000) if f(N) > 52))
#9774
# def perevod(n, s):
#     N = ''
#     while n: #так как n=0 - это то же самое что и false
#         N += str(n%s)
#         n //= s
#     return N[::-1]#шаг -1
# def f(N):
#     t = perevod(N, 3)
#     if N%3 == 0:
#         #t +=  ''.join(list(t)[-2:])
#         t += t[-2:]
#     else:
#         t += perevod((N%3) * 5, 3)
#     return int(t, 3)
# print(min([f(N) for N in range(1, 10000) if f(N) > 133]))

#Home_work
#4186
# def f(N):
#     b = bin(N)[2:]
#     if N%2 == 0:
#         b = '10' + b
#     else:
#         b = '1' + b + '01'
#     return int(b, 2)
# print(min([N for N in range(1, 10000) if f(N) > 441]))
#49
# def f(N):
#     b = bin(N)[2:]
#     b += str(b.count('1') % 2)
#     b += str(b.count('1') % 2)
#     return int(b, 2)
#
# print(min([f(N) for N in range(1, 10000) if f(N) > 80]))
# 557
# def f(N):
#     b = bin(N)[2:]
#     b += b[-1]
#     if b.count('1')%2 == 0:
#         b += '0'
#     else: b += '1'
#     if b.count('1')%2 == 0:
#         b += '0'
#     else: b += '1'
#     return int(b, 2)
# print(min([f(N) for N in range(1, 10000) if f(N)>144]))
# 975
# def f(N):
#     b = bin(N)[2:]
#     b += str(b.count('1')%2)
#     b += str(b.count('1')%2)
#     return int(b, 2)
# print(max([N for N in range(1, 10000) if f(N)<86]))
# 1958
# def f(N):
#     b = bin(N)[2:]
#     b += str(b.count('1')%2)
#     b += str(b.count('1')%2)
#     return int(b, 2)
# print(min([N for N in range(1, 10000) if f(N)>77]))
#31351
# def f(N):
#     b = bin(N)[2:]
#     if b.count('1')%2 ==0:
#         b = '10' + b[2:] + '0'
#     else:
#         b = '11' + b[2:] + '1'
#     return int(b, 2)
# print(min([N for N in range(1, 1000) if f(N) >= 16]))
#21243
# def p(n, s):
#     N = ''
#     while n:
#         N += str(n%s)
#         n //= s
#     return N[::-1]
# def f(N):
#     b = p(N, 5)
#     if sum(map(int, list(b)))%5 == 0:
#         b = b.replace('0', '5')
#         b = b.replace('1', '0')
#         b = b.replace('5', '1') + '14'
#     else:
#         b += '33'
#         b = '44' + b[2:]
#     return int(b, 5)
# R = min([f(N) for N in range(1, 10000) if f(N) > 370])
# print(*[N for N in range(1, 10000) if f(N) == R])
## R = 1000
## N_min = 1
## for N in range(1, 10000):
##     if R > f(N) and f(N) > 370:
##         R = f(N)
##         N_min = N
## print(N_min)
#29956
# def p(n):
#     N = ''
#     while n:
#         N += str(n%3)
#         n //= 3
#     return N[::-1]
# def f(N):
#     b = p(N)
#     if N%3 == 0:
#         b = '1' + b + '02'
#     else:
#         b += str(p((N%3)*5))
#     return int(b, 3)
# print(min(N for N in range(1, 10000) if f(N)>=177))
#8658
# def p(n):
#     N = ''
#     while n:
#         N += str(n%8)
#         n //= 8
#     return N[::-1]
# def f(N):
#     b = p(N)
#     if N%7 == 0:
#         b += b[-2:]
#     else:
#         b += p((N%7)*7)
#     return int(b, 8)
# print(sum(1 for N in range(1, 10000) if f(N)<3000))
#4317
# def p(n):
#     N=''
#     while n:
#         N += str(n%5)
#         n //= 5
#     return N[::-1]
# def f(N):
#     b = p(N)
#     if int(b[-1])%2 == 0:
#         b += '2'
#     else:
#         b = '2' + b + '3'
#     return int(b, 5)
# print(max(N for N in range(1, 10000) if f(N) < 1000))


#Home_Work_2
#4665
# def f(N):
#     b = bin(N)[2:]
#     if b.count('1')%2 == 0:
#         b += '1'
#         b = b.replace(b[:2], '10', 1)
#     else:
#         b += '0'
#         b = '11' + b[2:]
#     return int(b, 2)
# print(max(f(N) for N in range(1, 16)))
#4096
# def f(N):
#     b = bin(N)[2:]
#     if N%2==0:
#         b = '10'+b+'10'
#     else:
#         b = '1' + b + '00'
#     return int(b, 2)
# print(min(f(N) for N in range(1, 10000) if f(N)>100))
#9152
# def f(N):
#     b = bin(N)[2:]
#     if N%5==0:
#         b = '1' + b + b[:-2]
#     else:
#         b = bin(N%5)[2:] + b
#     return int(b, 2)
# print(max([f(N) for N in range(1, 10000) if f(N)<=223]))
#14329
# def p(n):
#     N =''
#     while n:
#         N += str(n%4)
#         n //= 4
#     return N[::-1]
# def f(N):
#     b = p(N)
#     if N%4==0:
#         b += b[:2]
#     else:
#         b += p((N%4)*4)
#     return int(b, 4)
# print(min([f(N) for N in range(1, 10000) if f(N)>291]) )
#16371
# def f(N):
#     b = bin(N)[2:]
#     if N%3 == 0:
#         b += b[-2:]
#     else:
#         b += bin(N%3 * 3)[2:]
#     return int(b, 2)
# print(min([f(N) for N in range(1, 10000) if f(N)>=195]))
#17518
# def f(N):
#     b = bin(N)[2:]
#     if b.count('1')%2==0:
#         b += '0'
#         b = b.replace(b[:2], '10', 1)
#     else:
#         b += '1'
#         b = '11' + b[2:]
#     return int(b, 2)
# print(min([N for N in range(1, 10000) if f(N)>50]))
#12914
# def f (N):
#     b = bin(N)[2:]
#     if N%3==0:
#         b = b.replace('0', '11')
#     else:
#         b = b.replace('1', '10')
#     return int(b, 2)
# print(max([f(N) for N in range(1, 10000) if f(N)<=161]))
#5723
# def f(N):
#     b = bin(N)[2:]
#     if b.count('1')%2 == 0:
#         b = '10' + b
#     else: b = '11' + b
#     if b.count('1') % 2 == 0:
#         b += '00'
#
#     else: b += '11'
#     return int(b, 2)
# print(len([f(N) for N in range(1, 1000) if f(N)<860]))
#8423
# def f(N):
#     b = bin(N)[2:]
#     if N%5==0:
#         b += bin(5)[2:]
#     else: b +='1'
#     if int(b, 2)%7 == 0:
#         b += bin(7)[2:]
#     else: b+='1'
#     return int(b, 2)
# print(max([N for N in range(1, 1000000) if f(N) < 1855663]))
#262
# def f(N):
#     b = bin(N)[2:]
#     b = '0'*(8-len(b)) + b
#     b = b.replace('0', '2').replace('1', '0').replace('2', '1')
#     return int(b, 2) + 1
# print(*[N for N in range(1, 128) if f(N)==221])


#31143
# def f(N):
#     b = bin(N)[2:]
#     if N%2 == 0:
#         b = '10' + b
#     else:
#         b = '1' + b + '01'
#     return int(b, 2)
# print(min([N for N in range(1, 10000) if f(N) >= 190]))

#21891
# def f(N):
#     b = bin(N)[2:]
#     b += str(b.count('1') % 2)
#     b += str(b.count('1') % 2)
#     return int(b, 2)
# [print(n) for n in range(1,1000) if f(n)>253]


# def f(n):
#     b = oct(n)[2:]
#     if n % 2 == 0:
#         b = '1' + b + '00'
#     else:
#         b = '10' + b + '1'
#     return int(int(b, 8))
#
#
# print(min([f(i) for i in range(1, 1000) if f(i) > 5566]))
def f(n):
    b = bin(n)[2:]
    if n%3==0:
        b+=b[-3:]
    else:
        b += bin((n%3)*3)[2:]
    return int(b, 2)
print(len([r for r in range(1, 10000) if f(r)<2311]))



















