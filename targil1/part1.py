

def getPentaNum(n):
    x=3*n
    y=x-1
    z=y*n
    return int(z/2)


def pentaNumRange(n1,n2):
    l=range(n1,n2)
    return map(getPentaNum,l)
    
        
        
pentaNumRange(1,28)
  
 


