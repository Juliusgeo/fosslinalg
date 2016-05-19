import numpy as np
global d, c
d=0
c=0
#requires numpy
#has a single argument m, which is a numpy matrix
#returns an integer
def determinant(m):
        if len(m)==2:
                #calculates the basic 2x2 matrix
                return (m.item(0,0)*m.item(1,1))-(m.item(1,0)*m.item(0,1))
        else:
                for s in range(0,len(m)):
                        #for every element in the top row it creates a matrix
                        #which is the original matrix without the top row and column
                        #in which the respective top row value resides
                        global d, c
                        w=np.delete(m,0,0)
                        w=np.delete(w,s,1)
                        d=((-1)**(s+2))*m.item(0,s)*determinant(w)
                        c=d+c
                return c
        

#print(determinant(np.matrix([[1, 2,4], [3, 4,4],[1,1,4]])))--the testing statement with a dummy matrix
