import numpy as np

def another_dot_product(vec1,vec2):
#This function is an example of how to
#compute a dot product
#INPUTS: vec1 and vec2 (1D lists, arrays)
#RETURNS: the dot product of 2 1D vectors
    mult=[]
    for i in range(0,len(vec1)):
        mult.append(vec1[i]*vec2[i]) 
    dot=np.sum(mult)
    return(dot)    
