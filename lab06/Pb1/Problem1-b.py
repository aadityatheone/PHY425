#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'Latin Modern Roman Demi','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams['figure.figsize']=[8,6]
#---
def A(x,h):
    return 1.

def B(x,h):
    return -2.

def C(x,h):
    return 1.

def fx(x,h):
    return -25.*h**2

def GE(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def FDM(xi,xf,a0,a1,b0,b1,g1,g2,n):
    h=(xf-xi)/(n+1)
    x=[]
    for i in range(n+1):
        x.append(xi+i*h)
    x.append(xf)
    O=np.zeros((n,n))
    O[0][0]=B(x[1],h)
    for i in range(1,n):
        O[i][i]=B(x[i+1],h)
        O[i-1][i]=A(x[i+1],h)
        O[i][i-1]=C(x[i],h)
    f=[fx(i,h) for i in x]
    if a1==0 and b1==0:
        M=O
        b=np.zeros(n)
        for i in range(n):
            b[i]=f[i+1]
        b[0]=b[0]-A(x[1],h)*g1
        b[n-1]=b[n-1]-C(x[n],h)*g2

        M=np.array(M)
        b=np.array(b)
        y=list(GE(np.hstack([M, b.reshape(-1, 1)])))
        y.insert(0,g1)
        y.insert(n,g2)
    elif a1==0 and b1!=0:
        M=np.zeros((n+1,n+1))
        b=np.zeros(n+1)
        for i in range(n):
            for j in range(n):
                M[i][j]=O[i][j]
        M[n][n]=B(x[n+1],h)-(2*h*b0/b1)*C(x[n+1],h)
        M[n-1][n]=C(x[n],h)
        M[n][n-1]=A(x[n+1],h)+C(x[n+1],h)
        for i in range(n+1):
            b[i]=f[i+1]
        b[0]=b[0]-A(x[1],h)*g1
        b[n]=b[n]-(2*h/b1)*C(x[n+1],h)*g2

        M=np.array(M)
        b=np.array(b)
        y=list(GE(np.hstack([M, b.reshape(-1, 1)])))
        y.insert(0,g1)
    elif a1!=0 and b1==0:
        M=np.zeros((n+1,n+1))
        b=np.zeros(n+1)
        for i in range(n):
            for j in range(n):
                M[i+1][j+1]=O[i][j]
        M[0][0]=B(x[0],h)-(2*h*a0/a1)*A(x[0],h)
        M[1][0]=A(x[1],h)
        M[0][1]=A(x[0],h)+C(x[0],h)
        for i in range(n+1):
            b[i]=f[i]
        b[0]=b[0]-(2*h/a1)*A(x[0],h)*g1
        b[n]=b[n]-C(x[n],h)*g2

        M=np.array(M)
        b=np.array(b)
        y=list(GE(np.hstack([M, b.reshape(-1, 1)])))
        y.insert(n+1,g2)
    elif a1!=0 and b1!=0:
        M=np.zeros((n+2,n+2))
        b=np.zeros(n+2)
        for i in range(n):
            for j in range(n):
                M[i+1][j+1]=O[i][j]
        M[0][0]=B(x[0],h)-(2*h*a0/a1)*A(x[0],h)
        M[1][0]=A(x[1],h)
        M[0][1]=A(x[0],h)+C(x[0],h)
        M[n+1][n+1]=B(x[n+1],h)-(2*h*b0/b1)*C(x[n+1],h)
        M[n][n+1]=C(x[n],h)
        M[n+1][n]=A(x[n+1],h)+C(x[n+1],h)
        for i in range(n+2):
            b[i]=f[i]
        b[0]=b[0]-(2*h/a1)*A(x[0],h)*g1
        b[n+1]=b[n+1]-(2*h/b1)*C(x[n+1],h)*g2
        print M
        M=np.array(M)
        b=np.array(b)
        y=list(GE(np.hstack([M, b.reshape(-1, 1)])))
    return x,y,h

xi=0.
xf=10.
g1=40.
g2=200.
a0,a1=1.,0.
b0,b1=1.,0.
n=399

x,y,h=FDM(xi,xf,a0,a1,b0,b1,g1,g2,n)

s=1
col=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]

plt.plot(x,y,color=col[0],linewidth=s,alpha=.6,label=r'$T(x)$',markersize=3*s)
plt.legend()
plt.xlabel(r'$x$')
plt.title(r' $h='+str(h)+'$')
plt.suptitle(r'Problem 1-b: Finite Difference Method')
plt.savefig("Figure1-b.png", dpi=300)
plt.clf()