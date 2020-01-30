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

def func1(t,x,y,z,pi,alp,bet,zet,delt):
    return pi-bet*x*y-delt*x

def func2(t,x,y,z,pi,alp,bet,zet,delt):
    return (bet-alp)*x*y+zet*z

def func3(t,x,y,z,pi,alp,bet,zet,delt):
    return delt*x+alp*x*y-zet*z

def RG4(t0,tf,x0,y0,z0,n,pi,alp,bet,zet,delt):
    t=[t0]
    x=[x0]
    y=[y0]
    z=[z0]
    h=(tf-t0)/float(n)
    for i in range(n):
        ti=t0+(i+1)*h
        k11=func1(t[i],x[i],y[i],z[i],pi,alp,bet,zet,delt)
        k21=func2(t[i],x[i],y[i],z[i],pi,alp,bet,zet,delt)
        k31=func3(t[i],x[i],y[i],z[i],pi,alp,bet,zet,delt)
        k12=func1(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,pi,alp,bet,zet,delt)
        k22=func2(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,pi,alp,bet,zet,delt)
        k32=func3(t[i]+.5*h,x[i]+.5*k11*h,y[i]+.5*k21*h,z[i]+.5*k31*h,pi,alp,bet,zet,delt)
        k13=func1(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,pi,alp,bet,zet,delt)
        k23=func2(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,pi,alp,bet,zet,delt)
        k33=func3(t[i]+.5*h,x[i]+.5*k12*h,y[i]+.5*k22*h,z[i]+.5*k32*h,pi,alp,bet,zet,delt)
        k14=func1(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,pi,alp,bet,zet,delt)
        k24=func2(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,pi,alp,bet,zet,delt)
        k34=func3(t[i]+h,x[i]+k13*h,y[i]+k23*h,z[i]+k33*h,pi,alp,bet,zet,delt)
        xi=x[i]+(k11+2*k12+2*k13+k14)*h/6
        yi=y[i]+(k21+2*k22+2*k23+k24)*h/6
        zi=z[i]+(k31+2*k32+2*k33+k34)*h/6
        t.append(ti)
        x.append(xi)
        y.append(yi)
        z.append(zi)
    return t,x,y,z,h

pi,alp,bet,zet,delt=0.0,0.005,.0095,.0001,.0001
t0=0
tf=10
S0=500
Z0=5
R0=0
n=20000
s=1
c=['red','darkorange','lime','green','purple','darkblue']
marker=["-o","-v","-P","-*"]
t1,S,Z,R,h=RG4(t0,tf,S0,Z0,R0,n,pi,alp,bet,zet,delt)
plt.plot(t1,S,color=c[4],linewidth=s,alpha=.7,label=r'$S$',markersize=3*s)
plt.plot(t1,Z,color=c[2],linewidth=s,alpha=.7,label=r'$Z$',markersize=3*s)
plt.plot(t1,R,color=c[0],linewidth=s,alpha=.7,label=r'$R$',markersize=3*s)
plt.xlabel(r'$t$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\pi='+str(pi)+'$'+r', $\alpha='+str(alp)+'$'+r', $\beta='+str(bet)+'$'+r', $\zeta='+str(zet)+'$'+r', $\delta='+str(delt)+'$')
plt.suptitle(r'Problem 5: Solving Zombie Population modeling using RG4 ($S$,$Z$,$R$ vs. $t$)')
plt.savefig("results/pr5_1.png", dpi=300)
plt.clf()
plt.plot(Z,S,color=c[3],linewidth=s,alpha=.7,label=r'$S(0)='+str(S0)+'$, $Z(0)='+str(Z0)+'$, $R(0)='+str(R0)+'$',markersize=3*s)
plt.xlabel(r'$Z$')
plt.ylabel(r'$S$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\pi='+str(pi)+'$'+r', $\alpha='+str(alp)+'$'+r', $\beta='+str(bet)+'$'+r', $\zeta='+str(zet)+'$'+r', $\delta='+str(delt)+'$')
plt.suptitle(r'Problem 5: Solving Zombie Population modeling using RG4 ($S$ vs. $Z$)')
plt.savefig("results/pr5_2.png", dpi=300)
plt.clf()
plt.plot(R,S,color=c[3],linewidth=s,alpha=.7,label=r'$S(0)='+str(S0)+'$, $Z(0)='+str(Z0)+'$, $R(0)='+str(R0)+'$',markersize=3*s)
plt.xlabel(r'$R$')
plt.ylabel(r'$S$')
plt.legend()
plt.title(r'$h='+str(h)+'$'+r', $t:'+str(t0)+r'\rightarrow '+str(tf)+'$'+r', $\pi='+str(pi)+'$'+r', $\alpha='+str(alp)+'$'+r', $\beta='+str(bet)+'$'+r', $\zeta='+str(zet)+'$'+r', $\delta='+str(delt)+'$')
plt.suptitle(r'Problem 5: Solving Zombie Population modeling using RG4 ($S$ vs. $R$)')
plt.savefig("results/pr5_3.png", dpi=300)
plt.clf()