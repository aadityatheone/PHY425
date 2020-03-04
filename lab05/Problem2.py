#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'Latin Modern Roman Demi','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams['figure.figsize']=[8,4]
#---
def func1(t,x,y):
    return y

def func2(t,x,y):
    return 48.*np.sin(10.*t)-12.*y-100.*x

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

def Adams(t0,tf,x0,y0,n):
    h=(tf-t0)/n
    t,x,y,h=RG5(t0,t0+4*h,x0,y0,4)
    yp=[]
    xp=[]
    for i in y:
        yp.append(i)
    for i in x:
        xp.append(i)
    for i in range(4,n):
        ti=t[i]+h

        xip=x[i]+h*(55.*func1(t[i],x[i],y[i])-59.*func1(t[i-1],x[i-1],y[i-1])+37.*func1(t[i-2],x[i-2],y[i-2])-9.*func1(t[i-3],x[i-3],y[i-3]))/24.
        yip=y[i]+h*(55.*func2(t[i],x[i],y[i])-59.*func2(t[i-1],x[i-1],y[i-1])+37.*func2(t[i-2],x[i-2],y[i-2])-9.*func2(t[i-3],x[i-3],y[i-3]))/24.

        xic=x[i]+h*(9.*func1(ti,xip,yip)+19.*func1(t[i],x[i],y[i])-5.*func1(t[i-1],x[i-1],y[i-1])+func1(t[i-2],x[i-2],y[i-2]))/24.
        yic=y[i]+h*(9.*func2(ti,xip,yip)+19.*func2(t[i],x[i],y[i])-5.*func2(t[i-1],x[i-1],y[i-1])+func2(t[i-2],x[i-2],y[i-2]))/24.
        xp.append(xip)
        x.append(xic)
        yp.append(yip)
        y.append(yic)
        t.append(ti)
    return t,xp,x,yp,y,h


t0=0.
tf=72.
x0=0
y0=0
t=np.linspace(t0,tf,100)
n=10000
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
t1,x1,y1,h1=RG5(t0,tf,x0,y0,n)
t2,x2p,x2,y2p,y2,h2=Adams(t0,tf,x0,y0,n)
plt.plot(t1,x1,color=c[0],linewidth=s,alpha=.6,label=r'$Q$',markersize=3*s)
plt.plot(t1,y1,color=c[2],linewidth=s,alpha=.6,label=r'$I$',markersize=3*s)
plt.legend()
plt.xlabel(r'$t$')
plt.title(r'$h='+str(h1)+'$')
plt.suptitle(r'Problem 2a: Explicit(RK5)')
# print h
plt.savefig("Figure2-a.png", dpi=300)
plt.clf()
plt.plot(t2,x2,color=c[0],linewidth=s,alpha=.6,label=r'$Q$',markersize=3*s)
plt.plot(t2,y2,color=c[2],linewidth=s,alpha=.6,label=r'$I$',markersize=3*s)
plt.legend()
plt.xlabel(r'$t$')
plt.title(r'$h='+str(h2)+'$')
plt.suptitle(r'Problem 2b: Implicit($4^{th}$ Order Adams-Moulton Method)')
# print h
plt.savefig("Figure2-b.png", dpi=300)
plt.clf()