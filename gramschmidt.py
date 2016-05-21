import numpy as np
m=np.matrix([[3,2],[1,2]])
def proj(a,b):
    return ((np.dot(a,b))/(np.dot(b,b)))
def a(i,k):
    if k==1:
        return 0
    else:
        k=k-1
        return proj(v[:,i],u[:,i-(1*k)])-a(i,k)
def gramschmidt(v):
    global u
    u=np.copy(v.astype(float))
    for i in range(0,len(m[0])):
        k=i
        u[:,i]=v[:,i]-proj(v[:,i],u[:,i-(1*k)])*b-a(i,k)
                
    for i in range(0,len(u[0])):
        norm=np.linalg.norm(u[:,i])
        print(norm)
        print(u[:,i])
        u[:,i]=u[:,i]/norm
    return u
print(gramschmidt(m))
