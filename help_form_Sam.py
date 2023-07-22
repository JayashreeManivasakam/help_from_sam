s=int(input())
a=1
count=1
while a < s:
    if a *2 <=s:
        a *= 2
    else:
        a+=1
        count +=1
print(count)
