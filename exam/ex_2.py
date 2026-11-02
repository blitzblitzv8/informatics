# from itertools import product, permutations
# def f(x,  y,  w, z):
#     return (z<= (not(y <= x))) or w
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7): #перебор всех значении в кажых х
#     t = {
#         (x1, 1, x2, x3, 0),
#         (x4, x5, 0, 0, 0),
#         (x6, 0, 1, x7, 0)
#     }
#     if len(t)==len(set(t)): #исключаем повторения
#         for p in permutations('xyzw'):#перестановка
#             if all(f(**dict(zip(p, line)))== line[-1] for line in t):#распаковываем склейку, кидаем её в функцию
#                 print(*p)

# from itertools import product, permutations
# def f(x, y, z, w):
#     return (w==z) or (x and(not y)) or w
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#     (x1, x2, 1, x3, 0),
#     (x4, 0, x5, x6, 0),
#     (x7, 1, 0, 0, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in t):
#                 print(''.join(p))

# from itertools import*
# def f(x, y, z, w):
#     return (x <= y) and z and (not w)
#
# for x1, x2, x3, x4 in product([0, 1], repeat=4):
#     t =(
#     (0, 1, x1, 1, 1),
#     (x2, 1, x3, x4, 1),
#     (0, 1, 1, 1, 1)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**(dict(zip(p, line))))==line[-1] for line in t):
#                 print(''.join(p))

# from itertools import*
# def f(x, y, z, w):
#     return (w or x or y) <= ((y or z) and x or y and(w or z))
# for x1, x2, x3,x4, x5 in product([0, 1], repeat=5):
#     t = (
#     (0, 0, 0, x1, 0),
#     (x2, 1, 1, x3, 0),
#     (x4, 1, x5, 1, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, line)))==line[-1] for line in t):
#                 print(''.join(p))

# from itertools import*
# def f(a, b, c, t):
#     return ((not a) or (not b)) and(c <= (not a)) and (t and (not a) or c and (not b))
#
# t = (
# (1, 0, 0, 1, 0),
# (1, 1, 0, 1, 1),
# (0, 0, 0, 1, 0),
# (1, 0, 0, 0, 1)
# )
#
# for p in permutations('abct'):
#     if all(f(**dict(zip(p, line)))==line[-1] for line in t):
#         print(''.join(p))

# from itertools import *
# def f(a, b, c):
#     return a and (not b) or c
# t=(
#     (0, 0, 0, 0),
#     (0, 0, 1, 1),
#     (0, 1, 0, 1),
#     (0, 1, 1, 1),
#     (1, 0, 0, 0),
#     (1, 0, 1, 0),
#     (1, 1, 0, 1),
#     (1, 1, 1, 1)
# )
# for p in permutations('abc'):
#     if all(f(**dict(zip(p, line)))==line[-1] for line in t):
#         print(''.join(p))


from itertools import*
# def f(x, y, z, w):
#     return (not ((((not w) <= (not y)) <= (not z)) <= x))
#
# for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
#     t = (
#     (x1, x2, 1, 0, 1),
#     (x3, 1, x4, 1, 1),
#     (0, 1, x5, 0, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, line)))==line[-1] for line in t):
#                 print(''.join(p))

# from itertools import*
# def f(x, y, z, w):
#     return (not(z <= x)) or (y <= w) or (not y)
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#     (0, 1, x1, x2, 0),
#     (x3, 0, x4, x5, 0),
#     (1, x6, 0, x7, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, line)))== line[-1] for line in t):
#                 print(''.join(p))

# from itertools import*
# def f(x, y, z, w):
#     return ((w == (not x)) <= (not(z <= w))) or (not y)
#
# for x1, x2, x3,x4,x5 in product([0, 1], repeat=5):
#     t = (
#     (x1, 0,1 ,0, 0),
#     (0, x2, x3, 0, 0),
#     (x4, 1, 1, x5, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in t):
#                 print(''.join(p))

# from itertools import *
# def f(x, y, z, w):
#     return (not((x <= w) <= (w == z))) and y
#
# for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
#     t= (
#     (x1, 0, 1, 0, 1),
#     (0, x2, x3, 0, 1),
#     (x4, 1, 1, x5, 1)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(''.join(p))

# from itertools import *
# def f(x, y, z, w):
#     return (z <= (not(y <= x))) or w
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#     (x1, 1, x2, x3, 0),
#     (x4, x5, 0, 0, 0),
#     (x6, 0, 1, x7, 0)
#     )
#     if len(t)== len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(''.join(p))
#3.33 минуты

from itertools import*
def f(x, y, z,w):
    return (not (y <= z)) or ((not x) <= (not w)) or x
for x1, x2, x3, x4, x5, x6 in product([0,1], repeat=6):
    t = (
    (x1, x2, x3, 0, 0),
    (0, x4, x5, 0, 0),
    (0, x6, 0, 0, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, m)))==m[-1] for m in t):
                print(''.join(p))



















































