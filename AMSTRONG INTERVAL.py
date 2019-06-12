
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
    
    
    


