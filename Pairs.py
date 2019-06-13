You will be given an array of integers and a target value. Determine the number
of pairs of array elements that have a difference equal to a target value.
For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition:
2-1=1,3-2=1 ,4-3=1.


Sample Input
5 2  
1 5 3 4 2  

Sample Output
3


***********************solution********************
def pairs(k, arr):
    c=0
    s=sorted(arr)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j]-s[i]==k:
                c=c+1
    return c
        
nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().split()))
print(pairs(k,arr))


*****************efficient method***********
def pairs(k, arr):
    c=0
    s=set(arr)
    for i in s:
        if i+k in s:
            c=c+1
    return c
        
        
nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().split()))
print(pairs(k,arr))


