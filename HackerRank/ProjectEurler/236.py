# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
from collections import deque

def has_solution(a,b,u,v):
    diva=v*a
    divb=u*b
    dd=math.gcd(divb,diva)
    sb=divb//dd
    sa=diva//dd
    if sb<=b and sa<=a:
        return True,sa,sb
    else:
        return False,-1,-1


def prod(a,b):
    s=0
    for i in range(len(a)):
        s+=a[i]*b[i]
    return s
            


n=int(input())

a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

#print(a)
#print(b)

u=2
v=1 

found=False

while found==False:

    works=True

    sa=[]
    sb=[]
    #print(u,v)

    for i in range(n):
        has,sai,sbi= has_solution(a[i],b[i],u,v)
        if has==False:
            works=False 
            break
        else:
            sa.append(sai)
            sb.append(sbi)

    #if u==10 and v==9:
    #    print(sa)
    #    print(sb)

    if works==True:

        #print(sa)
        #print(sb)

        suma=sum(a)
        sumb=sum(b)

        hyp=deque([]) 

        hyp_n=0
        mults=[1 for _ in range(n)]

        hyp.append([sum(sa),sum(sb)])

        while hyp_n<n:
            if ((mults[hyp_n]+1)*sa[hyp_n]<=a[hyp_n] and\
             (mults[hyp_n]+1)*sb[hyp_n]<=b[hyp_n]):

                mults[hyp_n]+=1 
                for i in range(hyp_n):
                    mults[i]=1
                hyp.append([prod(mults,sa),prod(mults,sb)])
                hyp_n=0 
                
            else:
                hyp_n+=1
        
        #print(hyp)
        while len(hyp)>0:
            h=hyp.popleft()
            if h[0]*sum(b)*v==h[1]*sum(a)*u:
                found=True 
                break

        if found==True:
            break  


    #NEXT HYPOTHESIS
    v+=1
    while math.gcd(u,v)>1:
        v+=1
    
    if v>=u:
        u+=1
        v=1 


print("{}/{}".format(u,v))

