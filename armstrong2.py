print("armstrong numbers between 100 and 999 are")
list=[]
sum=0
for num in range(100,999):
    orinum=num
    while(num>0):
        digit=num%10
        sum=sum+(digit*digit*digit)
        num/=10
    if(sum==orinum):
        list.append(orinum)

print(list)


