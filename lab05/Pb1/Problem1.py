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
def func1(t,x,y,g,p):
    return y

def func2(t,x,y,g,p):
    return g-p*y

def F(x,xf):
    return x[len(x)-1]-xf

def RG5(t0,tf,x0,y0,n,g,p):
    t=[t0]
    x=[x0]
    y=[y0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i],g,p)
        k21=func2(t[i],x[i],y[i],g,p)
        k12=func1(t[i]+.25*h,x[i]+.25*k11*h,y[i]+.25*k21*h,g,p)
        k22=func2(t[i]+.25*h,y[i]+.25*k11*h,y[i]+.25*k21*h,g,p)
        k13=func1(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,g,p)
        k23=func2(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h,g,p)
        k14=func1(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,g,p)
        k24=func2(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h,g,p)
        k15=func1(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,g,p)
        k25=func2(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h,g,p)
        k16=func1(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,g,p)
        k26=func2(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h,g,p)
        xi=x[i]+(7*k11+32*k13+12*k14+32*k15+7*k16)*h/90
        yi=y[i]+(7*k21+32*k23+12*k24+32*k25+7*k26)*h/90
        t.append(ti)
        x.append(xi)
        y.append(yi)
    return t,x,y,h

def shoot(t0,tf,x0,xf,n,g,p,a0,a1,tol):
    t1,x1,y1,h1=RG5(t0,tf,x0,a0,n,g,p)
    t2,x2,y2,h2=RG5(t0,tf,x0,a1,n,g,p)
    i=0
    while(np.abs(a1-a0)>tol):
        ai=a1
        a1=a1-((a1-a0)/(F(x2,xf)-F(x1,xf)))*F(x2,xf)
        a0=ai
        t1,x1,y1,h1=RG5(t0,tf,x0,a0,n,g,p)
        t2,x2,y2,h2=RG5(t0,tf,x0,a1,n,g,p)
        i=i+1
    
    return t2,x2,y2,h2,i

c=12.5
m=70.
p=c/m
g=9.8
x0=0.
xf=500.
a0=40.
a1=100.
tol=0.000001
n=100000
t0=0.
tf=12.

t,x,y,h,i=shoot(t0,tf,x0,xf,n,g,p,a0,a1,tol)

s=1
col=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]

plt.plot(t,x,color=col[1],linewidth=s,alpha=.6,label=r'$Position$',markersize=3*s)
plt.plot(t,y,color=col[3],linewidth=s,alpha=.6,label=r'$Velocity$',markersize=3*s)
plt.legend()
plt.xlabel(r'$t$')
plt.title(r'$\alpha_0='+str(a0)+'$'+r', $\alpha_1='+str(a1)+'$'+r', $\alpha_f='+str(y[0])+'$'+r', $h='+str(h)+'$'+r'        |Completed in '+str(i)+r' iterations')
plt.suptitle(r'Problem 1: Shooting Method')
plt.savefig("Figure1.png", dpi=300)
plt.clf()