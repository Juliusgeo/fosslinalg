import numpy as np
m=np.matrix([[1,1,1,1],[1,1,1,1],[0,1,2,3],[0,1,2,3]])
def swap(m, row1, row2):
    c=np.copy(m[0:,0:])
    c[row2]=m[row1]
    c[row1]=m[row2]
    return c

def rref(m):
    i=0
    j=i
    while i<=len(m)-1 and j<=len(m[0]):
        print(i)
        print(j)
        if m.item(i,j) == 0:
            for n in range(i,len(m)):
                if swap(m,i,i+n).item(i,j) !=0:
                    m=np.copy(swap(m,i,i+n))
        m[i]=np.copy(m[i]/m.item(i,j))
        p=0
        for k in range(i+1,len(m)):
                while m.item(k,j)==0 and p<len(m):
                    if m.item(p,j) != 0 and m.item(k,j) != 0:
                        if m[k]+(m.item(p,j)/m.item(k,j))*m[p] ==0:
                            m[k]=m[k]+(m.item(p,j)/m.item(k,j))*m[p]
                        else:
                            m[k]=m[k]-(m.item(p,j)/m.item(k,j))*m[p]
                    p+=1
        i+=1
        j+=1
    return m
                
