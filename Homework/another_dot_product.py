import numpy as np

def another_dot_product(vec1,vec2):
    mult=[]
    for i in range(0,len(vec1)):
        mult.append(vec1[i]*vec2[i]) 
    dot=np.sum(mult)
    return(dot)    
