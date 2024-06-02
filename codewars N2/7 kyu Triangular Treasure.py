def triangular(n):
    result=0
    if n <= 0:
        return result
    elif n>=1:
        result=(n*(n+1))//2
        return result
        