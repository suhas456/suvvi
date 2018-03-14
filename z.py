#gcd and lcm
m=int(input('enetr m value'))
n=int(input('enetr n value'))
a=m
b=n
while (n!=0):
    r=m%n
    m=n
    n=r

print('gcd of',a,'and',b,'is',m)
print('lcm of',a,'and',b,'is',a*b//m)    
#or
x=10
y=20
def gcd(u,v):   
    while (v!=0):
        p=u%v
        u=v
        v=p
    return u
print('gcd of',x,'and',y,'is',gcd(x,y))
print('lcm of',x,'and',y,'is',x*y//gcd(x,y))
