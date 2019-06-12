
You are given a string containing characters  and  only. Your task is to change it into a string
such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more 
characters in the string.Your task is to find the minimum number of required deletions.
For example, given the string , remove an  at positions  and  to make  in deletions.


Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output
3
4
0
0
4

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ANS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def alternatingCharacters(s):
    l=len(s)
    c=0
    for i in range(0,l-1):
        if s[i]==s[i+1]:
            c=c+1
    return c
    
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
