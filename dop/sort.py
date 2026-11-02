# def bin_search(arr, value):
#     lower_bound = 0
#     upper_bound = len(arr) - 1
#     i = 0
#     while lower_bound <= upper_bound:
#         i += 1
#         mid = (lower_bound + upper_bound) // 2
#         mid_value = arr[mid]
#
#         if mid_value == value:
#             return print(i)
#         elif value > mid_value:
#             lower_bound = mid+1
#         elif value < mid_value:
#             upper_bound = mid-1
#
#     return print('число не найдено')
#
# arr = [3, 4, 5, 7, 9, 10, 13, 15, 45, 46, 47, 48, 39, 233, 345, 456, 567, 678, 789]
# bin_search(arr, 234)

def swap(arr, a, b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c
    return arr

#сортировка выбором
# def selection_sort(arr , n):
#
#     for i in range(0, n):
#         min = arr[i]
#         min_i = i
#
#         for j in range(i, n):
#             if arr[j] < min:
#                 min = arr[j]
#                 min_i = j
#         swap(arr, i, min_i)
#     return arr
#
# arr = [3, 2, 4, 23, 64, 75, 345, 34, 4, 63, 63234, 643, 214, 0]
# print(selection_sort(arr, len(arr)))

# сортировка пузырьком

def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        flag = 0

        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                flag = 1
        if not flag:
            break
    return print(arr)

arr = [3, 2, 4, 23, 64, 75, 345, 34, 4, 63, 63234, 643, 214, 0]
print(bubble_sort(arr))

