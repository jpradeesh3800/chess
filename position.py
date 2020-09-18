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

