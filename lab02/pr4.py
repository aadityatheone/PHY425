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

def func1(t,x,y,a,b):
    return -a*x

def func2(t,x,y,a,b):
    return -func1(t,x,y,a,b)-b*y


def RG5(t0,tf,x0,y0,n,a,b):
    t=[t0]
    x=[x0]
    y=[y0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i],a,b)
        k21=func2(t[i],x[i],y[i],a,b)
        k12=func1(t[i]+.25*h,x[i]+.25*k11*h,y[i]+.25*k21*h,a,b)
        k22=func2(t[i]+.25*h,y[i]+.25*k11*h,y[i]+.25*k21*h,a,b)
        k13=func1(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,a,b)
        k23=func2(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,a,b)
        k14=func1(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,a,b)
        k24=func2(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,a,b)
        k15=func1(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,a,b)
        k25=func2(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,a,b)
        k16=func1(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,a,b)
        k26=func2(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,a,b)
        xi=x[i]+(7*k11+32*k13+12*k14+32*k15+7*k16)*h/90
        yi=y[i]+(7*k21+32*k23+12*k24+32*k25+7*k26)*h/90
        t.append(ti)
        x.append(xi)
        y.append(yi)
    return t,x,y,h

t0=0.
tf=20
x0=1000000.
y0=0.
h0=1.
tol=.05
a=1.
n=10000
b=.25*a
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,x1,y1,h=RG5(t0,tf,x0,y0,n,a,b)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$X$',markersize=3*s)
plt.plot(t1,y1,color=c[4],linewidth=s,alpha=.7,label=r'$Y$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $k_1='+str(a)+'$'+r', $k_2='+str(b)+'$')
plt.suptitle(r'Problem 4: Solving Radioactive Decay Equations using RG5 ($X$, $Y$ vs. $t$)')
plt.savefig("results/pr4_1.png", dpi=300)
plt.clf()
b=a
t1,x1,y1,h=RG5(t0,tf,x0,y0,n,a,b)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$X$',markersize=3*s)
plt.plot(t1,y1,color=c[4],linewidth=s,alpha=.7,label=r'$Y$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $k_1='+str(a)+'$'+r', $k_2='+str(b)+'$')
plt.suptitle(r'Problem 4: Solving Radioactive Decay Equations using RG5 ($X$, $Y$ vs. $t$)')
plt.savefig("results/pr4_2.png", dpi=300)
plt.clf()
b=2*a
t1,x1,y1,h=RG5(t0,tf,x0,y0,n,a,b)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$X$',markersize=3*s)
plt.plot(t1,y1,color=c[4],linewidth=s,alpha=.7,label=r'$Y$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $k_1='+str(a)+'$'+r', $k_2='+str(b)+'$')
plt.suptitle(r'Problem 4: Solving Radioactive Decay Equations using RG5 ($X$, $Y$ vs. $t$)')
plt.savefig("results/pr4_3.png", dpi=300)
plt.clf()