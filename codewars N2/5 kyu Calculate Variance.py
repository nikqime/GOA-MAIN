def variance(numbers): 
    sum_of_nums=sum(numbers)
    lenght=len(numbers)
    mean=sum_of_nums/lenght
    
    for_var=[(i-mean)**2 for i in numbers]
    variance=sum(for_var)/len(for_var)
    return variance