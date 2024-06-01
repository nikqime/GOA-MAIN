def solution(s):
    if len(s) % 2 != 0:
        s+="_" 
    
    babe=[s[i:i+2]for i in range (0 , len(2), 2)]
    return babe

def solution(s):
    
    if len(s) % 2 != 0:
        s += '_'
   
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    return pairs

