******************************MAKING ANAGRAMS***************************
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?
Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
For example,  and . The only characters that match are the 's so we have to remove  from  and  from  for a total of  deletions.

Sample Input
cde
abc

Sample Output
4

Explanation
We delete the following characters from our two strings to turn them into anagrams of each other:
Remove d and e from cde to get c.
Remove a and b from abc to get c.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ANS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def makingAnagrams(s1, s2):
    c=list(set(s1+s2))
    l1=collections.Counter(s1)
    l2=collections.Counter(s2)
    c2=0
    for i in c:
        c2+=abs(l1[i]-l2[i])
    return c2

s1 = input()
s2 = input()
result = makingAnagrams(s1, s2)
print(result)








**********************************ALTERNATING CHARACTERS****************************
You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
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
