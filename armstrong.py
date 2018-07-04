number=int(input("enter number "))
temp=number
sum=0
while(temp>0):
    rem=temp%10
    sum=sum+(rem*rem*rem)
    temp=int(temp/10)

if(number==sum):
    print("Armstrong")
else:
    print("Not")