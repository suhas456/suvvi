#user defined fuctions
def add(a,b):
    return a+b
print(add(2,3))
def sub(a,b):
    return a-b
print(sub(2,3))
def multiply(a,b):
    return a*b
print(multiply(2,3))
def div(a,b):
    return a//b
print(div(2,3))
def floatdiv(a,b):
    return a/b
print(floatdiv(2,3))
def modulus(a,b):
    return a%b
print(modulus(2,3))
def gcd(a,b):
    while (b!=0):
        r=a%b
        a=b
        b=r
    return a 
print('gcd of 10,30 is',gcd(10,30))
print('lcm of 10,30 is',(10*30)//gcd(10,30))


