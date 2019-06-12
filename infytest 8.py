**************************************AMSTRONG INTERVAL*************************************************
Write a program to display Armstrong numbers between two intervals

Sample Input 0
100
1000

Sample Output 
153
370
371
407

^^^^^^^^^^^^^^^^^^^ANS^^^^^^^^^^^^^^^^^^^^
start=int(input())
end=int(input())
for i in range(start,end):
    t=i
    r=0
    k=len(str(i))
    while(i!=0):
        s=i%10
        r=r+s**k
        i=i//10
    
    if(t==r):
        print(t)
    
    
    


***************************************NUM TO ROMAN *********************************************8
Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and 
returns the equivalent roman numeral of it.
e.g.(890->DCCCXC; 88->LXXXVIII)

Symbol | Value
I : 1
V : 5
X : 10
L : 50
C : 100
D : 500
M : 1,000

^^^^^^^^^^^^^^^^^^ANS^^^^^^^^^^^^^
def ntor(n):
    nl=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    rl=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    l=[]
    r=""
    i=0
    while n>0:
        for _ in range(n//nl[i]):
            r+=rl[i]
            n-=nl[i]
        i=i+1
    return r 
    
n=int(input())
print(ntor(n))




*******************************ROMAN TO NUM********************************
Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and
returns the equivalent roman numeral of it.
Symbol | Value
I : 1
V : 5
X : 10
L : 50
C : 100
D : 500
M : 1,000

^^^^^^^^^^^^^^^^ANS^^^^^^^^^^^^^^^^^^^^^
def value(r):
    if(r=='I'):
        return 1
    if r=='V':
        return 5
    if(r=='X'):
        return 10
    if r=='L':
        return 50
    if r=='C':
        return 100
    if r=='D':
        return 500
    if r=='M':
        return 1000
    
def rtod(n):
    i=0
    a=0
    while(i<len(n)):
        s1=value(n[i])
        if(i+1<len(n)):
            s2=value(n[i+1])
            if(s1>=s2):
                a=a+s1
                i=i+1
            else:
                a=a+s2-s1
                i=i+2
        else:
            a=a+s1
            i=i+1
    return a
n=input()
print(rtod(n))
