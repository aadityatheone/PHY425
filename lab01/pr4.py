#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
#---
def func(x,y):
    return -x*y**2
def euler(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        yi=y[i]+h*func(x[i],y[i])
        x.append(xi)
        y.append(yi)
    return x,y,h
def ihuen(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        yi0=y[i]+h*func(x[i],y[i])
        for j in range(1000):
            yi=y[i]+h*(func(x[i],y[i])+func(xi,yi0))/2
            if abs(yi-yi0)>0.001:
                # print (yi-yi0), ((2/(1+xi**2))-yi)
                yi0=yi
            else:
                y.append(yi)
                break
        x.append(xi)
    return x,y,h
def huen(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        yi0=y[i]+h*func(x[i],y[i])
        yi=y[i]+h*(func(x[i],y[i])+func(xi,yi0))/2
        x.append(xi)
        y.append(yi)
    return x,y,h
def midpoint(x0,xf,y0,n):
    x=[x0]
    y=[y0]
    h=(xf-x0)/float(n)
    for i in range(n):
        xi=x0+(i+1)*h
        ximp=x[i]+h/2
        yimp=y[i]+h*func(x[i],y[i])/2
        yi=y[i]+h*func(ximp,yimp)
        x.append(xi)
        y.append(yi)
    return x,y,h
x0=0
xf=10

#---plot---

x=np.linspace(x0,xf,100)
y=2/(1+x**2)
n=20
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
ex,ey,h=euler(x0,xf,2,n)
hx,hy,h=huen(x0,xf,2,n)
mpx,mpy,h=midpoint(x0,xf,2,n)
plt.plot(x,y,linewidth=s,label=r'$y=\frac{2}{1+x^2}$',color='blue')
plt.plot(ex,ey,marker[0],color=c[0],linewidth=s,alpha=.7,label=r'Euler for $h='+str(h)+'$',markersize=3*s)
plt.plot(hx,hy,marker[1],color=c[1],linewidth=s,alpha=.7,label=r'Huen for $h='+str(h)+'$',markersize=3*s)
plt.plot(mpx,mpy,marker[2],color=c[2],linewidth=s,alpha=.7,label=r'Mid-point for $h='+str(h)+'$',markersize=3*s)
print h
plt.ylim(-0.1,2.1)
plt.legend()
plt.title(r'Problem 4: Mid-point Method')
plt.show()
