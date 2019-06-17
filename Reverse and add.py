def reverse(num):
    return int(str(num)[::-1])

def palindrome(num):
    for i in range(100):
        rnum = reverse(num)
        if rnum == num:
            break
        num = num + rnum
    return i, num

num=int(input())
print(*(palindrome(num)))
