from pack import filr

class adddetails:
    def __init__(self):
        pass
    def details(self):
        name = input("enter name")
        print()
        email = input("enter email")
        print()
        accnum = input("enter account num")
        print()
        age = input("enter age")
        print()
        bank = input("enter bank name")
        print()
        r.deposit(name,email,accnum,age,bank)

    def showdetails(self,name,email,accnum,age,bank):
       return self.name+" "+self.email
a=adddetails()

r=filr.account()
while True:
    i=int(input("enter"))
    if(i==1):
        a.details()

        break
    elif(i==2):
        a.showdetails()
        break

    else:
        print("invalid")
        break


