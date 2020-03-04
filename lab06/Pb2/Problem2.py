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

def f(x):
    return np.sin(np.pi*x)

def SchM(xi,xf,ti,tf,g1,g2,nx,nt):
    h=(xf-xi)/nx
    k=(tf-ti)/nt
    l=k/h**2
    x,t=[],[]
    for i in range(nx+1):
        x.append(xi+i*h)
    for j in range(nt+1):
        t.append(ti+j*k)
    u=np.zeros((nt+1,nx+1))
    for i in range(nx+1):
        u[0][i]=f(x[i])
    for j in range(nt+1):
        u[j][0]=g1
        u[j][nx]=g2
    for j in range(nt):
        for i in range(1,nx):
            u[j+1][i]=l*u[j][i-1]+(1-2*l)*u[j][i]+l*u[j][i+1]
    return x,t,u,h,k

xi,xf,ti,tf=0.,1.,0.,1.
nt,nx=36,3
g1,g2=0.,0.
x,y,u,h,k=SchM(xi,xf,ti,tf,g1,g2,nx,nt)
np.savetxt('Result.txt',u,fmt='%.2f')
plt.pcolor(x,y,u,cmap='jet')
plt.colorbar().set_label(r'$u(x,t)$', fontsize=12)
plt.xlabel(r'$x$')
plt.ylabel(r'$t$')
plt.title(r' $h='+str(h)+'$'+r', $k='+str(k)+'$')
plt.suptitle(r'Problem 2: Schmidt Method')
plt.savefig("Figure2.png", dpi=600, bbox_inches='tight')
plt.clf()