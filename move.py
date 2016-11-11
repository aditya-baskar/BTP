def check(x,y,r,c):
    if x<0 or x>=r or y<0 or y>=c:
        return 0
    return 1

def dist(a,b,c,d):
    return abs(c-a)+abs(d-b)

def move(xpos,ypos,speed,endxpos,endypos,matrix,rows,columns):
    newx=0
    newy=0
    min_dis=1000000
    for k in xrange(speed):
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i)+abs(j)!=1 or check(xpos+i,ypos+j,rows,columns)==0 or matrix[xpos+i][ypos+j]==0:
                    continue
                newdis=dist(xpos+i,ypos+j,endxpos,endypos)
                if(newdis<min_dis):
                    newx=xpos+i
                    newy=ypos+j
                    min_dis=newdis
        xpos=newx
        ypos=newy
    return (xpos,ypos)
            
