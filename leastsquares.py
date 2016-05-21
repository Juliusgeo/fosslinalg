import numpy as np
#a=np.matrix([[-1,2],[2,-3],[-1,3]])
#b=np.matrix([[4],[1],[2]])
def leastsquares(a,b):
    x=((a.transpose()*a).getI())*(a.transpose()*b)
    answer=""
    for i in range(0,len(x)):
        answer+="x"+str((i+1))+"="+str(x[i])+" , "
    return answer
