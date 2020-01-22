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
    return 1.1*x-0.4*x*y

def func2(t,x,y):
    return .1*x*y-.4*y

def RG5(t0,tf,x0,y0,n):
    t=[t0]
    x=[x0]
    y=[y0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i])
        k21=func2(t[i],x[i],y[i])
        k12=func1(t[i]+.25*h,x[i]+.25*k11*h,y[i]+.25*k21*h)
        k22=func2(t[i]+.25*h,y[i]+.25*k11*h,y[i]+.25*k21*h)
        k13=func1(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h)
        k23=func2(t[i]+.25*h,x[i]+.125*k12*h+.125*k11*h,y[i]+.125*k22*h+.125*k21*h)
        k14=func1(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h)
        k24=func2(t[i]+.5*h,x[i]-.5*k12*h+k13*h,y[i]-.5*k22*h+k23*h)
        k15=func1(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h)
        k25=func2(t[i]+.75*h,x[i]+.1875*k11*h+.5625*k14*h,y[i]+.1875*k21*h+.5625*k24*h)
        k16=func1(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h)
        k26=func2(t[i]+h,x[i]-(3./7)*k11*h+(2./7)*k12*h+(12./7)*k13*h-(12./7)*k14*h+(8./7)*k15*h,y[i]-(3./7)*k21*h+(2./7)*k22*h+(12./7)*k23*h-(12./7)*k24*h+(8./7)*k25*h)
        xi=x[i]+(7*k11+32*k13+12*k14+32*k15+7*k16)*h/90
        yi=y[i]+(7*k21+32*k23+12*k24+32*k25+7*k26)*h/90
        t.append(ti)
        x.append(xi)
        y.append(yi)
    return t,x,y,h

t0=0
tf=200
x0=100
y0=5
n=20000
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,x1,y1,h=RG5(t0,tf,x0,y0,n)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$x(t)$',markersize=3*s)
plt.plot(t1,y1,color=c[1],linewidth=s,alpha=.7,label=r'$y(t)$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:0\rightarrow 200$')
plt.suptitle(r'Problem 3: Solving Lotka-Voltera Equations using RG5 ($x$, $y$ vs. $t$)')
plt.savefig("results/pr3_1.png", dpi=300)
plt.clf()
plt.plot(x1,y1,color=c[1],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$',markersize=3*s)
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:0\rightarrow 200$')
plt.suptitle(r'Problem 3: Solving Lotka-Voltera Equations using RG5 ($y$ vs. $x$)')
plt.savefig("results/pr3_2.png", dpi=300)
plt.clf()
for i in range(6):
    x0=100+i*200
    y0=10
    t1,x1,y1,h=RG5(t0,tf,x0,y0,n)       
    plt.plot(x1,y1,color=c[i],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$',markersize=3*s)
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.suptitle(r'Problem 3: Solving Lotka-Voltera Equations using RG5 ($y$ vs. $x$)')
plt.title(r'$h='+str(h)+'$'+r', $x(0):100\rightarrow 1000$'+r', $t:0\rightarrow 200$')
plt.savefig("results/pr3_3.png", dpi=300)
plt.clf()
for i in range(6):
    x0=200
    y0=5+i*20
    t1,x1,y1,h=RG5(t0,tf,x0,y0,n)       
    plt.plot(x1,y1,color=c[i],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$',markersize=3*s)
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.suptitle(r'Problem 3: Solving Lotka-Voltera Equations using RG5 ($y$ vs. $x$)')
plt.title(r'$h='+str(h)+'$'+r', $y(0):5\rightarrow 100$'+r', $t:0\rightarrow 200$')
plt.savefig("results/pr3_4.png", dpi=300)
plt.clf()
