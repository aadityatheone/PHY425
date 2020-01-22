#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams["figure.figsize"] = [9,6]
plt.subplots_adjust(left=0.1, right=0.7)
#---

def func(x,y):
    return -(1+y**2)/(1+x**2)
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
                # print (yi-yi0), (((1-xi)/(1+xi))-yi)
                yi0=yi
            else:
                y.append(yi)
                break
        x.append(xi)
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
x0=0.0
xf=15.0
y0=1.0

#---plot---

x=np.linspace(x0,xf,100)
y=(1-x)/(1+x)
n=[15,20,30]
s=1
c=['red','purple','green','darkorange']
marker=["-o","-v","-P","-*"]
plt.plot(x,y,linewidth=s,label=r'$y=\frac{1-x}{1+x}$',color='blue')
for i in range(len(n)):
    hx,hy,h=huen(x0,xf,y0,n[i])
    plt.plot(hx,hy,marker[1],color=c[1],linewidth=s,alpha=float(i+1)/(len(n)),label=r'Simple Huen for $h='+str(h)+'$',markersize=3*s)

for i in range(len(n)):
    ex,ey,h=ihuen(x0,xf,y0,n[i])
    plt.plot(ex,ey,marker[0],color=c[0],linewidth=s,alpha=float(i+1)/(len(n)),label=r'Huen with iteration for $h='+str(h)+'$',markersize=3*s)

for i in range(len(n)):
    mpx,mpy,h=midpoint(x0,xf,y0,n[i])
    plt.plot(mpx,mpy,marker[2],color=c[2],linewidth=s,alpha=float(i+1)/(len(n)),label=r'Mid-point for $h='+str(h)+'$',markersize=3*s)
# print h
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title(r'Problem 5')
plt.show()
