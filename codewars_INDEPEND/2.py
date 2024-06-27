def all_nines(x):
    if x % 2 == 0:
        return -1
    num_of_nines = 1
    current_value = 9 % x 
    while current_value != 0:
        num_of_nines += 1
        current_value = (current_value * 10 + 9) % x
    return int('9' * num_of_nines)