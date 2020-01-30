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

def func1(t,x,y,z,sig,b,r):
    return -sig*x+sig*y

def func2(t,x,y,z,sig,b,r):
    return r*x-y-x*z

def func3(t,x,y,z,sig,b,r):
    return -b*z+x*y

def RG4(t0,tf,x0,y0,z0,n,sig,b,r):
    t=[t0]
    x=[x0]
    y=[y0]
    z=[z0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i],z[i],sig,b,r)
        k21=func2(t[i],x[i],y[i],z[i],sig,b,r)
        k31=func3(t[i],x[i],y[i],z[i],sig,b,r)
        k12=func1(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,sig,b,r)
        k22=func2(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,sig,b,r)
        k32=func3(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,sig,b,r)
        k13=func1(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,sig,b,r)
        k23=func2(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,sig,b,r)
        k33=func3(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,sig,b,r)
        k14=func1(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,sig,b,r)
        k24=func2(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,sig,b,r)
        k34=func3(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,sig,b,r)
        xi=x[i]+(k11+2*k12+2*k13+k14)*h/6
        yi=y[i]+(k21+2*k22+2*k23+k24)*h/6
        zi=z[i]+(k31+2*k32+2*k33+k34)*h/6
        t.append(ti)
        x.append(xi)
        y.append(yi)
        z.append(zi)
    return t,x,y,z,h

sig,b,r=10.0,2.66667,28.0
t0=0
tf=50
x0=5
y0=5
z0=5
n=20000
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,x1,y1,z1,h=RG4(t0,tf,x0,y0,z0,n,sig,b,r)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$',markersize=3*s)
plt.xlabel(r'$t$')
plt.ylabel(r'$x(t)$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\sigma='+str(sig)+'$'+r', $b='+str(b)+'$'+r', $r='+str(r)+'$')
plt.suptitle(r'Problem 2: Solving Lorenz Equations using RG4 ($x$ vs. $t$)')
plt.savefig("results/pr2_1.png", dpi=300)
plt.clf()
plt.plot(y1,x1,color=c[4],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$, $z(0)='+str(z0)+'$',markersize=3*s)
plt.xlabel(r'$y(t)$')
plt.ylabel(r'$x(t)$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\sigma='+str(sig)+'$'+r', $b='+str(b)+'$'+r', $r='+str(r)+'$')
plt.suptitle(r'Problem 2: Solving Lorenz Equations using RG4 ($x$ vs. $y$)')
plt.savefig("results/pr2_2.png", dpi=300)
plt.clf()
plt.plot(z1,x1,color=c[4],linewidth=s,alpha=.7,label=r'$x(0)='+str(x0)+'$, $y(0)='+str(y0)+'$, $z(0)='+str(z0)+'$',markersize=3*s)
plt.xlabel(r'$z(t)$')
plt.ylabel(r'$x(t)$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\sigma='+str(sig)+'$'+r', $b='+str(b)+'$'+r', $r='+str(r)+'$')
plt.suptitle(r'Problem 2: Solving Lorenz Equations using RG4 ($x$ vs. $z$)')
plt.savefig("results/pr2_3.png", dpi=300)
plt.clf()

