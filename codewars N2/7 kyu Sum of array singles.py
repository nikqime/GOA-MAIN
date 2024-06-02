def repeats(arr):
    result=0
    mellstroy={}
    
    for i in arr:
        if i in mellstroy:
            mellstroy[i]+=1
        elif i not in mellstroy:
            mellstroy[i]=1
            
    for i in mellstroy:
        if mellstroy[i]==1:
            result +=i
            
    return result