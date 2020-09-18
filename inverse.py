from math import atan2,sin,cos,acos
def theta(x,y,z,a,l1,l2,l3):

    # theta1
    t1=atan2(y,x)

    # 
    d=(x**2+y**2)**0.5
    s=l3*sin(a)
    c=l3*cos(a)

    # f=square ,g=square root
    f=lambda x:x**2
    g=lambda x:x**0.5

    x1=z+s
    y1=d-c

    x2= f(d-c) + f(z+s) + f(l1) - f(l2)
    y2=2*l1*g( f(f(d)-c) + f(z+s) )

    # theta2
    t2=atan2(x1,y1)+acos(x2/y2)

    x3=f(l1) + f(l2) - f(d-c) - f(z+s)
    y3=2*l1*l2

    # theta3
    t3=acos(x3/y3)

    k=[t1,t2,t3]

    k=list(map(lambda x:str(int(x)).zfill(3),k))

    return "".join(k)
    
def position(i,f):
    x0=
    y0=
    l0=
    xi=x0+i[0]*l0+(l0/2)
    yi=y0+i[1]*l0+(l0/2)
    zi=0

    initial=theta(xi,yi,zi,90)

    xf=x0+f[0]*l0+(l0/2)
    yf=y0+f[1]*l0+(l0/2)
    zf=0

    final=theta(xf,yf,zf,90)

    return initial+final


if __name__=="__main__":
    x,y,z,a,l1,l2,l3=(1,2,3,4,5,6,7)
    t1,t2,t3=theta(x,y,z,a,l1,l2,l3)
    print(t1,t2,t3)