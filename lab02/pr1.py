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
    return -(1+y**2)/(1+x**2)

def RG2(x0,xf,y0,n,a1):
    x=[x0]
    y=[y0]
    a2=1-a1
    p1=0.5/a2
    q11=p1
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        k1=func(x[i],y[i])
        k2=func(x[i]+p1*h,y[i]+q11*k1*h)
        yi=y[i]+(a1*k1+a2*k2)*h
        x.append(xi)
        y.append(yi)
    return x,y,h

def RG3(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        k1=func(x[i],y[i])
        k2=func(x[i]+.5*h,y[i]+.5*k1*h)
        k3=func(x[i]+h,y[i]-k1*h+2*k2*h)
        yi=y[i]+(k1+4*k2+k3)*h/6
        x.append(xi)
        y.append(yi)
    return x,y,h

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

def RG5(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        k1=func(x[i],y[i])
        k2=func(x[i]+.25*h,y[i]+.25*k1*h)
        k3=func(x[i]+.25*h,y[i]+.125*k2*h+.125*k1*h)
        k4=func(x[i]+.5*h,y[i]-.5*k2*h+k3*h)
        k5=func(x[i]+.75*h,y[i]+.1875*k1*h+.5625*k4*h)
        k6=func(x[i]+h,y[i]-(3./7)*k1*h+(2./7)*k2*h+(12./7)*k3*h-(12./7)*k4*h+(8./7)*k5*h)
        yi=y[i]+(7*k1+32*k3+12*k4+32*k5+7*k6)*h/90
        x.append(xi)
        y.append(yi)
    return x,y,h

x0=0
xf=10
y0=1
a1=1./3.
x=np.linspace(x0,xf,100)
y=(1-x)/(1+x)
n=10
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
plt.plot(x,y,linewidth=s,label=r'$y=\frac{1-x}{1+x}$',color='blue')
x1,y1,h=RG2(x0,xf,y0,n,a1)
plt.plot(x1,y1,marker[0],color=c[0],linewidth=s,alpha=.7,label=r'$RG2$($\textbf{Ralston`s Method}$)',markersize=3*s)
x2,y2,h=RG3(x0,xf,y0,n)
plt.plot(x2,y2,marker[1],color=c[1],linewidth=s,alpha=.7,label=r'$RG3$',markersize=3*s)
x3,y3,h=RG4(x0,xf,y0,n)
plt.plot(x3,y3,marker[2],color=c[2],linewidth=s,alpha=.7,label=r'$RG4$',markersize=3*s)
x4,y4,h=RG5(x0,xf,y0,n)
plt.plot(x4,y4,marker[3],color=c[3],linewidth=s,alpha=.7,label=r'$RG5$',markersize=3*s)
plt.legend()
plt.title(r'$h='+str(h)+'$')
plt.suptitle(r'Problem 1: $RG$ $Method$')
print h
plt.savefig("results/pr1_1.png", dpi=300)
plt.clf()