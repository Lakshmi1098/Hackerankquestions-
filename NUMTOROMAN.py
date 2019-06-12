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



