def calculator(q,n, operacia):
    if operacia == '+':
        return q + n
    elif operacia == '-':
        return q - n
    elif operacia == '*':
        return q * n
    elif operacia == '/':
        return q / n
print(calculator(7, 3, '+'))
print(calculator(9, 4, '-'))        
print(calculator(164, 45, '*'))     
print(calculator(69, 1488, '/'))           
    