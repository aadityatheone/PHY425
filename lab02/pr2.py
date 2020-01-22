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

def func(x,y):
    return x*(1-y**3)/(3*y**2)

def RKF45(x0,xf,y0,h0,t):
    x=[x0]
    y=[y0]
    h=h0
    i=0
    while(x[i]<xf-h):
        xi=x[i]+h
        k1=h*func(x[i],y[i])
        k2=h*func(x[i]+.25*h,y[i]+.25*k1)
        k3=h*func(x[i]+.375*h,y[i]+.09375*k1+.28125*k2)
        k4=h*func(x[i]+0.923076923*h,y[i]+0.879380974*k1-3.277196177*k2+3.320892126*k3)
        k5=h*func(x[i]+h,y[i]+2.032407407*k1-8.*k2+7.173489279*k3-0.205896686*k4)
        k6=h*func(x[i]+.5*h,y[i]-0.296296296*k1+2.*k2-1.381676413*k3+0.45297271*k4-(11./40)*k5)
        yi4rk=y[i]+(0.115740741*k1+0.548927875*k3+0.50613149*k4-.2*k5)
        yi5rk=y[i]+(0.118518519*k1+0.518986355*k3+0.50613149*k4-0.18*k5+0.036363636*k6)
        err=abs(yi5rk-yi4rk)
        if err>=1.5*t*yi5rk:
            h=h/2
        elif err<=.5*t*yi5rk:
            x.append(xi)
            y.append(yi5rk)
            h=2*h
            i+=1
        else:
            x.append(xi)
            y.append(yi5rk)
            i+=1

    return x,y,h

x0=0
xf=15
y0=2
x=np.linspace(x0,xf,100)
y=(1+7*np.exp(-0.5*x**2))**(1./3.)
h0=.1
t=0.01      #TOLERENCE FACTOR
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
plt.plot(x,y,linewidth=s,label=r'$y=(1+7e^{-x^2/2})^{1/3}$',color='blue')
x1,y1,h=RKF45(x0,xf,y0,h0,t)
plt.plot(x1,y1,marker[0],color=c[0],linewidth=s,alpha=.7,label=r'RKF45',markersize=3*s)
plt.legend()
plt.title(r'Problem 2: RKF45 Method')
plt.savefig("results/pr2_1.png", dpi=300)
plt.clf()