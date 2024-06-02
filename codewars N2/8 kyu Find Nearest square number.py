def nearest_sq(n):
    vaime_es_raari= int(n**0.5)
    
    lw= vaime_es_raari*vaime_es_raari
    up= (vaime_es_raari+1)* (vaime_es_raari+1)
    
    if vaime_es_raari>0:
        lw_2=(vaime_es_raari-1)    * (vaime_es_raari-1)
    else:
        lw_2=lw
    
    if (n- lw)<=(up-n):
        if (n-lw_2) < (n-lw):
            return lw_2
        return lw
    else:
        return up