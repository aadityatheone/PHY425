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

def func1(t,x,y):
    return y

def func2(t,x,y):
    if t==0:
        return -x
    else:
        return -x-y/t

def RG5(t0,tf,x0,y0,n):
    t=[t0]
    x=[x0]
    y=[y0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i] )
        k21=func2(t[i],x[i],y[i] )
        k12=func1(t[i]+.25*h,x[i]+.25*k11*h,y[i]+.25*k21*h )
        k22=func2(t[i]+.25*h,y[i]+.25*k11*h,y[i]+.25*k21*h )
        k13=func1(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h )
        k23=func2(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h )
        k14=func1(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h )
        k24=func2(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h )
        k15=func1(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h )
        k25=func2(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h )
        k16=func1(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h )
        k26=func2(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h )
        xi=x[i]+(7*k11+32*k13+12*k14+32*k15+7*k16)*h/90
        yi=y[i]+(7*k21+32*k23+12*k24+32*k25+7*k26)*h/90
        t.append(ti)
        x.append(xi)
        y.append(yi)
    return t,x,y,h

def Gears(t0,tf,x0,y0,n):
    h=(tf-t0)/n
    t,x,y,h=RG5(t0,t0+5*h,x0,y0,5)
    yp=[]
    xp=[]
    for i in range(len(x)):
        yp.append(y[i])
        xp.append(x[i])
    for i in range(5,n):
        ti=t[i]
        xi=(300./137.)*xp[i-1]-(300./137.)*xp[i-2]+(200./137.)*xp[i-3]-(75./137.)*xp[i-4]+(12./137.)*xp[i-5]+(60./137.)*h*func1(ti,xp[i],yp[i])
        yi=(300./137.)*yp[i-1]-(300./137.)*yp[i-2]+(200./137.)*yp[i-3]-(75./137.)*yp[i-4]+(12./137.)*yp[i-5]+(60./137.)*h*func2(ti,xp[i],yp[i])
        x.append(xi)
        y.append(yi)
        xp.append(xi)
        yp.append(yi)
        t.append(ti+h)
    return t,x,y,h


t0=0.
tf=15.
x0=1.
y0=0    
n=2000
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,x1,y1,h=Gears(t0,tf,x0,y0,n  )
# print t1,x1
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,markersize=3*s)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $x:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $y(0)='+str(x0)+'$'+r', $y^\prime(0)='+str(y0)+'$', fontsize=10)
plt.suptitle(r'Problem 1: Solving $\frac{d^2y}{dx^2}+\frac{1}{x}\frac{dy}{dx}+y=0$ using Gear`s Method')
plt.savefig("results/pr1_1.png", dpi=300)
plt.clf()