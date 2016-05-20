import numpy as np
m=np.matrix([[1,2,2],[3,4,4],[2,2,2]])
def swap(m, row1, row2):
    c=np.copy(m[0:,0:])
    c[row2]=m[row1]
    c[row1]=m[row2]
    return c

def rref(m):
    i=0
    j=i
    while i<=len(m) & j<=len(m[0]):
        if m.item(i,j) == 0:
            for n in range(i,len(m)):
                if swap(m,i,i+n).item(i,j) !=0:
                    m=np.copy(swap(m,i,i+n))

        m[i]=np.copy(m[i]/m.item(i,j))
    
        for k in range(i,len(m[0])):
            for p in range(i, len(m[0])):
                if m.item(p,j)%m.item(k,j)==0:
                    #if m.item(p,j)<m.item(k,j):
                    m[k]=m[k]+(m.item(p,j)/m.item(k,j))*m[p]
                    #else:
  #                      m[k]=m[k]+(m.item(p,j)/m.item(k,j))*m[p]
        i+=1
        j+=1
    return m
                
