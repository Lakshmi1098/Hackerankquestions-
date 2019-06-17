def int_to_words(t):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
    '11 : 'eleven', 12 : 'twelve', 13 :'thirteen', 14 : 'fourteen',15 : 'fifteen', 16 : 'sixteen', 
    17 : 'seventeen', 18 : 'eighteen',19 : 'nineteen', 20 : 'twenty',30 :'thirty',40 : 'forty', 50 : 'fifty',
    60 : 'sixty',70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
    if(k>4):
        return -1
    if(t<20):
        return (d[t])
    if(t<100):
        if(t%10==0):
            return (d[t])
        else:
            return d[t//10*10]+" "+d[t%10]
    if(t<1000):
        if(t%100==0):
            return d[t//100]+" "+"hundred"
        else:
            return d[t//100]+" "+"hundred and"+" "+int_to_words(t%100)
    if(t==1000):
        return("one thousand")
    if(t>1000):
        return(-1)
n=int(input())
k=len(str(n))
t=int(n)
print(int_to_words(t))
    
