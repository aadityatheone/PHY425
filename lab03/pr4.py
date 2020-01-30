#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'Latin Modern Roman Demi','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams['figure.figsize']=[6,4]
#---
def func(t,y):
    return -2*y/(1+t)

def RG4(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        k1=func(x[i],y[i])
        k2=func(x[i]+.5*h,y[i]+.5*k1*h)
        k3=func(x[i]+.5*h,y[i]+.5*k2*h)
        k4=func(x[i]+h,y[i]+k3*h)
        yi=y[i]+(k1+2*k2+2*k3+k4)*h/6
        x.append(xi)
        y.append(yi)
    return x,y,h

def Adams(t0,tf,y0,n):
    h=(tf-t0)/n
    t,y,h=RG4(t0,t0+4*h,y0,4)
    yp=[]
    for i in y:
        yp.append(i)
    for i in range(4,n):
        ti=t[i]+h
        yip=y[i]+h*(55.*func(t[i],y[i])-59.*func(t[i-1],y[i-1])+37.*func(t[i-2],y[i-2])-9.*func(t[i-3],y[i-3]))/24.
        yic=y[i]+h*(9.*func(ti,yip)+19.*func(t[i],y[i])-5.*func(t[i-1],y[i-1])+func(t[i-2],y[i-2]))/24.
        yp.append(yip)
        y.append(yic)
        t.append(ti)
    return t,yp,y,h


t0=0
tf=2.5
y0=2
t=np.linspace(t0,tf,100)
y=2*(1+t)**(-2)
n=10
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
plt.plot(t,y,linewidth=s,label=r'$y=\frac{2}{(1+t)^2}$',color='blue')
t1,y1p,y1,h=Adams(t0,tf,y0,n)
plt.plot(t1,y1p,marker[0],color=c[0],linewidth=s,alpha=.6,label=r'$y^P$',markersize=3*s)
plt.plot(t1,y1,marker[1],color=c[2],linewidth=s,alpha=.6,label=r'$y^C$',markersize=3*s)
plt.legend()
plt.title(r'$h='+str(h)+'$')
plt.suptitle(r'Problem 4: $4^{th}$ order Adams Method')
# print h
plt.savefig("results/pr4_1.png", dpi=300)
plt.clf()