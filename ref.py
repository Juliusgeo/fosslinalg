import numpy as np

def swap(m, row1, row2):
    c=np.copy(m[0:,0:])
    c[row2]=m[row1]
    c[row1]=m[row2]
    return c

def trim(m):
    c=np.copy(m[0:,0:])
    a=[True]
    b=False
    i=0
    while i<=m.shape[1]:
        for j in range(0,m.shape[0]):
            if m.item(j,i)!=0:
                if i==0:
                    return c
                else:
                    b=True
                    break
        if b:
            break
        i+=1
    for j in range(0,i):
        a=np.append(a,False)
    for j in range(i,m.shape[1]):
        a=np.append(a,True)
    a=np.delete(a,0)
    c=np.compress(a,c,axis=1)
    return c

def ref(m):
    if m.shape[0]==1:
        for i in range(1,m.shape[1]):
            m[0,i]=m.item(0,i)/m.item(0,0)
        m[0,0]=1
        return m
    m=np.copy(trim(m))
    if m.item(0,0)==0:
        for i in range(1,m.shape[0]):
            if m.item(i,0)!=0:
                m=np.copy(swap(m,0,i))
                break
    for i in range(1,m.shape[1]):
        m[0,i]=m.item(0,i)/m.item(0,0)
    m[0,0]=1
    for j in range(1,m.shape[0]):
        for k in range(1,m.shape[1]):
            m[j,k]=m.item(j,k)-(m.item(j,0))*(m.item(0,k))
        m[j,0]=0
    a=[False]
    b=[False]
    for i in range(1,m.shape[0]):
        a=np.append(a,True)
    for i in range(1,m.shape[1]):
        b=np.append(b,True)
    n=np.compress(a,np.compress(b,m,axis=1),axis=0)
    n=np.copy(rref2(n))
    for i in range(1,m.shape[0]):
        for j in range(1,m.shape[1]):
            m[i,j]=n.item(i-1,j-1)
    return m

	
def rref(m):
	m=np.copy(ref(m))
	
	
	
	
	
	
	