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
x0=0
xf=10

#---plot---

x=np.linspace(x0,xf,100)
y=2/(1+x**2)
n=[20,25,50]
s=1
c=['red','darkorange','lime','green']
marker=["-o","-v","-P","-*"]
plt.plot(x,y,linewidth=s,label=r'$y=\frac{2}{1+x^2}$')
for i in range(len(n)):
    ex,ey,h=euler(x0,xf,2,n[len(n)-1-i])
    plt.plot(ex,ey,marker[i],color=c[len(n)-1-i],linewidth=s,alpha=.7,label=r'$h='+str(h)+'$',markersize=3*s)
plt.legend()
plt.title(r'Problem 3: Euler`s Method')
print h
plt.show()
plt.clf()
plt.plot(x,y,linewidth=s,label=r'$y=\frac{2}{1+x^2}$',color='blue')
for i in range(len(n)):
    hx,hy,h=huen(x0,xf,2,n[len(n)-1-i])
    plt.plot(hx,hy,marker[i],color=c[len(n)-1-i],linewidth=s,alpha=.7,label=r'$h='+str(h)+'$',markersize=3*s)
plt.legend()
plt.title(r'Problem 3: Simple Huen`s Method')
print h
plt.show()
plt.clf()
plt.plot(x,y,linewidth=s,label=r'$y=\frac{2}{1+x^2}$',color='blue')
hx,hy,h=huen(x0,xf,2,20)
ex,ey,h=euler(x0,xf,2,20)
plt.plot(hx,hy,marker[0],color=c[3],linewidth=s,alpha=.7,label=r'Huen for $h='+str(h)+'$',markersize=3*s)
plt.plot(ex,ey,marker[1],color=c[0],linewidth=s,alpha=.7,label=r'Euler for $h='+str(h)+'$',markersize=3*s)
plt.legend()
plt.title(r'Problem 3')
print h
plt.show()

