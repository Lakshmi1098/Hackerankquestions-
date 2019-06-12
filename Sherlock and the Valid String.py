For example, if s=abc, it is a valid string because frequencies are {a:1,b:1,c:1}. So is s=abcc because we can
remove one and have  of each character in the remaining string. If s=abccc however, the string is not valid
as we can only remove  occurrence of . That would leave character frequencies of {a:1,b:1,c:2}.



**********************ANS***************
s=input()
s=''.join(sorted(s))
res=0
l,j=[],{}
for i in s:
    res=s.count(i)
    if(res!=0):
        l.append(res)
        j[i]=res
    s=s.replace(i,"")

if((l.count(l[0]))==len(j)-1) or ((l.count(l[0]))==len(j)):
    print("YES")
else:
    print("NO")
  
   
