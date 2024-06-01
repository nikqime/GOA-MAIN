def count_all_elements(arr):
    result = 0
    for number in arr:
        result ^= number
    return result

