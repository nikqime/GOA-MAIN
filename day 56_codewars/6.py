q=int(input("Enter first number here: "))
y=int(input("Enter second number here: "))
def first_n_multiples(q, y):
    multiples = []
    for i in range(1, y + 1):
        multiples.append(q * i)
    return multiples
result=first_n_multiples(q, y)
print(result)