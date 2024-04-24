def multiply_array_values(arr):
    result = 1
    for num in arr:
        result *= num
    return result

array = [1, 2, 3, 4, 5]
result = multiply_array_values(array)
print("Result of multiplying the values in the array:", result)
