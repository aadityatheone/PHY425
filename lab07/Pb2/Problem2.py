#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import tensorflow
rc('font',**{'family':'Latin Modern Roman Demi','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams['figure.figsize']=[7,5]
plt.rcParams['figure.facecolor']='w'
from mpl_toolkits import mplot3d
from matplotlib.tri import Triangulation
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
#---

def f1(x):
    return x*(x-1.)

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

def RM(xi,xf,ti,tf,g1,g2,nx,nt):
    h=(xf-xi)/nx
    k=(tf-ti)/nt
    l=k/h**2
    print h,k
    x,t=[],[]
    for i in range(nx+1):
        x.append(xi+i*h)
    for j in range(nt+1):
        t.append(ti+j*k)
    u=np.zeros((nt+1,nx+1))
    for i in range(nx+1):
        u[0][i]=f1(x[i])
    for j in range(nt+1):
        u[j][0]=g1
        u[j][nx]=g2
    A=np.zeros((nx-1,nx-1))
    B=np.zeros((nx-1,nx-1))
    b=np.zeros(nx-1)
    for i in range(nx-1):
        if i==0:
            A[i,:]=[2+2*l if j==0 else -l if j==i+1 else 0 for j in range(nx-1)]
            B[i,:]=[2-2*l if j==0 else l if j==i+1 else 0 for j in range(nx-1)]
            b[i]=g1
        elif i==nx-2:
            A[i,:]=[2+2*l if j==i else -l if j==i-1 else 0 for j in range(nx-1)]
            B[i,:]=[2-2*l if j==i else l if j==i-1 else 0 for j in range(nx-1)]
            b[i]=g2
        else:
            A[i,:]=[2+2*l if j==i else -l if j==i-1 or j==i+1 else 0 for j in range(nx-1)]
            B[i,:]=[2-2*l if j==i else l if j==i-1 or j==i+1 else 0 for j in range(nx-1)]
    for j in range(2):
        uj=np.zeros(nx-1)
        for i in range(nx-1):
            uj[i]=u[j][i+1]
        d=B.dot(uj)+b
        un=GE(np.hstack([A, d.reshape(-1, 1)]))
        for i in range(nx-1):
            u[j+1][i+1]=un[i]
    for j in range(2,nt):
        for i in range(1,nx):
            u[j+1][i]=u[j-1][i]+2*l*(u[j][i-1]-2*u[j][i]+u[j][i+1])
    return x,t,u,h,k,l

xi,xf,ti,tf=0.,1.,0.,6./36.
nt,nx=6,6
g1,g2=0.,0.
x,y,u,h,k,l=RM(xi,xf,ti,tf,g1,g2,nx,nt)
np.savetxt('Result2.txt',u,fmt='%.2f')
plt.pcolor(x,y,u,cmap='jet')
plt.colorbar().set_label(r'$u(x,t)$', fontsize=12)
plt.xlabel(r'$x$')
plt.ylabel(r'$t$')
plt.title(r' $h='+str(h)+'$'+r', $k='+str(k)+'$'+r', $\lambda='+str(l)+'$')
plt.suptitle(r'Problem 2: Richardson`s method')
plt.savefig("Figure2.png", dpi=600, bbox_inches='tight')
plt.clf()