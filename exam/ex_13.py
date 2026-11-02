# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#
#     x1 = str(x)
#     if '1' in x1:
#         x1 = x1.replace('1', '2')
#         x1 = int(x1)
#     else: x1 = int(x1)
#
#     return f(x+1, end) + x1
# print(f(11, 92))
#не правильно
from string import ascii_uppercase, ascii_lowercase, ascii_letters

# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#
#     x1 = str(x)
#     if x1.count('1') > 0:
#         x1 = int(x1.replace('1', '2'))
#
#     else: x1 = end + 1
#
#     return f(x + 1, end) + f(x1, end)
# print(f(11, 92))

#315110 через арифметику
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#
#     if (x % 10) > (x % 100)//10:
#         x1 = (x // 100)*100 + (x % 10)*10 + (x % 100)//10
#     else: x1 = end + 1
#     return f(x + 1, end) + f(x1, end)
#
# print(f(100, 141))

#315110 через срезы
# def f(x, end):
#     if x > end:
#         return 0
#     if x == end:
#         return 1
#
#     x1 = str(x)
#       #объект[start:stop:step]
#     if x1[-1:] > x1[-2:-1]: #мы можем сравнивать строки так как символы расположены в определенном порядке в таблице ascii
#         x1 = int(x1[:-2] + x1[-1]+x1[-2])
#     else: x1 = end+1
#     return f(x+1, end) + f(x1, end)
#
# print(f(100, 141))

#29977
# def f(x, end):
#     if x < end  or x == 9: return 0
#     if x == end: return 1
#
#     return f(x-1, end) + f(x-3, end) + f(x//2, end)
# print(f(19, 12) * f(12, 3))

#home_work_5_october
#16387
# def f(x, end):
#     if x> end or x ==16: return 0
#     if x == end: return 1
#
#     return f(x+1, end) + f(x + 2, end) + f(x*3, end)
#
# print(f(2, 9) * f(9, 18))
#16387
# def f(x, end):
#     if x> end or x ==14: return 0
#     if x == end: return 1
#
#     return f(x + 1, end) + f(x + 3, end)
# print(f(2, 9) * f(9, 18))
#473
# def f(x, end):
#     if x > end or x == 43:
#         return 0
#     if x == end: return 1
#
#     return f(x + 2, end) + f(x + x - 1, end) + f(x + x +1, end)
#
# print(f(7, 63))
#504
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     x1 = int(str(x)+'1')
#     return f(x + 2, end) + f(x + 3, end) + f(x1, end)
# print(f(3, 12) * f(12, 25))
#11264
# def f(x, end):
#     if x > end or x == 32: return 0
#     if x == end: return 1
#     return f(x+2, end) + f(x+4, end)
# print(f(9, 27)*f(27, 29)*f(29, 37))
#3084
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     x1 = list(str(x))
#     x1 = sum(map(int, x1))
#
#     return f(x + 2, end) + f(x+x1, end)
# print(f(3, 29) * f(29, 68))
#18600
# def f(x, end, n):
#     if x > end or x == n: return 0
#     if x == end: return 1
#
#     return f(x+1, end, n) + f(x * 2, end, n) + f(x * 3, end, n)
#
# print(f(10, 30, 60) * f(30, 70, 60) + f(10, 60, 30) * f(60, 70, 30))
#24804
# def f(x, end, n):
#     if x > end or x == n: return 0
#     if x == end: return 1
#     if n == 1 and (x == 4 or x == 16): return 0
#     return f(x * 2, end, n) + f(x **2, end, n) + f(x ** 3, end, n)
# print(f(2, 131072, 4) + f(2, 131072, 16) - f(2, 131072, 1))
#31418
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     x1 = bin(x)[2:].count('1')
#     return f(x + 1, end) + f(x + x1, end)
# print(f(5, 40))
#31416
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     x1 = list(str(x))
#     x1 = int(str(x1[-1] + ''.join(x1[:-1])))
#     if x1 > x:
#         return f(x + 1, end) + f(x1, end)
#     return f(x + 1, end)
# print(f(102, 500))


#9376
# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#
#     return f(x + 1, end) + f(x + 2, end) + f(x*3, end)
#
# print(f(6, 15) * f(15, 25) + f(6, 21)*f(21, 25) - 2 * f(6, 15) * f(15, 21) * f(21, 25))

#3583
# def f(x, end):
#     if x == end: return 1
#     if x > end: return 0
#
#     return  f(x+2, end) + f(x*2, end)
# print(f(1, 24) * f(24, 50))

#1376
# def f(x, end):
#     if x == end: return 1
#     if x < end: return  0
#     return f(x - 8, end) + f(x // 2, end)
# print(f(102, 43) * f(43, 5))

#10104
# def f(x, end):
#     if x == end:
#         return 1
#     if x > end  or x == 11: return  0
#
#     return f(x + 1, end) + f(x * 2, end) + f(x**2, end)
# print(f(2, 20))

#278
# def f(x, end):
#     if x == end: return  1
#     if x > end: return  0
#     x1 = str(x)
#     if x1[-2] != '9':
#         x1 = str(x + 10)
#     else: x1 = str(end + 1)
#
#     return  f(x + 1, end) + f(int(x1), end)
#
# print(f(10, 33))

#104
#print((638-300)/2)

# 1140
# def perevod(n):
#     N = ''
#     while n:
#         N += str(n%3)
#         n //= 3
#     return int(N[::-1])
# def f(x, end):
#     if x == end: return 1
#     if x < end: return 0
#     x1 = perevod(int(str(x), 3) - 2)
#     x2 = str(x)
#     if x2[-1] != '0':
#         x2 = int(x2[:-1] + '0')
#     else: x2 = 0
#     return f(x1, end) + f(x2, end)
#
# print(f(212, 10))

#12930
def f(x, end):
    if x==end: return 1
    if x > end or x == 11 or x == 12: return 0
    return f(x+1, end) + f(x*2, end) + f(x**2, end)
print(f(2, 10)*f(10, 40))





