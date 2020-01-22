def taylor(x,x0,y0):
    y1=[]
    y1.append(-x0*y0**2)
    y1.append(-y0**2-2*x0*y0*y1[0])
    y1.append(-4*y0*y1[0]-2*x0*y1[0]**2-2*x0*y0*y1[1])
    y1.append(-6*y1[0]**2-6*y1[0]*y1[1]-6*x0*y1[0]*y1[1]-2*x0*y0*y1[2])
    fx=y0
    n=1
    for i in range(4):
        n*=i+1
        fx+=(x**(i+1)/n)*y1[i]
    return fx
print taylor(0.2,0,2)