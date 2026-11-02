def bin_search(arr, value):
    lower_bound = 0
    upper_bound = len(arr) - 1
    i = 0
    while lower_bound <= upper_bound:
        i += 1
        mid = (lower_bound + upper_bound) // 2
        mid_value = arr[mid]

        if mid_value == value:
            return print(i)
        elif value > mid_value:
            lower_bound = mid+1
        elif value < mid_value:
            upper_bound = mid-1

    return print('число не найдено')

arr = [3, 4, 5, 7, 9, 10, 13, 15, 45, 46, 47, 48, 39, 233, 345, 456, 567, 678, 789]
bin_search(arr, 234)

