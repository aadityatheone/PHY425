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

def func1(t,x,y,g,l):
    return y

def func2(t,x,y,g,l):
    return -(g/l)*np.sin(x)

def RG5(t0,tf,x0,y0,n,g,l):
    t=[t0]
    x=[x0]
    y=[y0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i],g,l)
        k21=func2(t[i],x[i],y[i],g,l)
        k12=func1(t[i]+.25*h,x[i]+.25*k11*h,y[i]+.25*k21*h,g,l)
        k22=func2(t[i]+.25*h,y[i]+.25*k11*h,y[i]+.25*k21*h,g,l)
        k13=func1(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,g,l)
        k23=func2(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,g,l)
        k14=func1(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,g,l)
        k24=func2(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,g,l)
        k15=func1(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,g,l)
        k25=func2(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,g,l)
        k16=func1(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,g,l)
        k26=func2(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,g,l)
        xi=x[i]+(7*k11+32*k13+12*k14+32*k15+7*k16)*h/90
        yi=y[i]+(7*k21+32*k23+12*k24+32*k25+7*k26)*h/90
        t.append(ti)
        x.append(xi)
        y.append(yi)
    return t,x,y,h
g,l=9.8,10
t0=0
tf=50
x0=1
y0=0
n=20000
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,x1,y1,h=RG5(t0,tf,x0,y0,n,g,l)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$\theta(t)$',markersize=3*s)
plt.plot(t1,y1,color=c[4],linewidth=s,alpha=.7,label=r'$\dot{\theta}(t)$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+r's$'+r', $g='+str(g)+r'ms^{-2}$'+r', $l='+str(l)+r'm$')
plt.suptitle(r'Problem 3: Solving Pendulum using RG5 ($\theta$, $\dot{\theta}$ vs. $t$)')
plt.savefig("results/pr3_1.png", dpi=300)
plt.clf()
plt.plot(x1,y1,color=c[2],linewidth=s,alpha=.7,label=r'$\theta(0)='+str(x0)+r'$, $\dot{\theta}(0)='+str(y0)+'$',markersize=3*s)
plt.xlabel(r'$\theta(t)$')
plt.ylabel(r'$\dot{\theta}(t)$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+r's$'+r', $g='+str(g)+r'ms^{-2}$'+r', $l='+str(l)+r'm$')
plt.suptitle(r'Problem 3: Solving Pendulum Equations using RG5 ($\dot{\theta}$ vs. $\theta$)')
plt.savefig("results/pr3_2.png", dpi=300)
plt.clf()