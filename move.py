def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def check(x,y,r,c):
    if x<0 or x>=r or y<0 or y>=c:
        return 0
    return 1

def dist(a,b,c,d):
    return abs(c-a)+abs(d-b)

def move(xpos,ypos,speed,endxpos,endypos,matrix,rows,columns,vision):
    print "here"
    newx=0
    newy=0
    min_dis=1000000
    flag=0
    vis = matrix
    for i in rows:
        for j in columns:
            vis[i][j]=0
    for k in xrange(speed):
        if xpos==endxpos and ypos==endypos:
            flag=1
            break
        for i in range(-1,2):
            for j in range(-1,2):
                if vis[xpos+i][ypos+j] == 1:
                    continue
                if abs(i)+abs(j)!=1 or check(xpos+i,ypos+j,rows,columns)==0 or matrix[xpos+i][ypos+j]=='x' or RepresentsInt(matrix[xpos+i][ypos+j]):
                    continue
                vis[xpos+i][ypos+j]=1
                newdis=dist(xpos+i,ypos+j,endxpos,endypos)
                if(newdis<min_dis):
                    newx=xpos+i
                    newy=ypos+j
                    min_dis=newdis
        xpos=newx
        ypos=newy
    if flag == 1:
        return (xpos,ypos)
    else:
        return (-1,-1)
            
