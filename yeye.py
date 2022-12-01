import json

userlist={}
savemovies=[]
customerlist=open("try.json","r")
customer=json.load(customerlist)
print(customer)

  
username=input("enter your email address: ")

for y in customer:
        if y["Email"]==username:
            print (username)
            print(y["Age"])
            print(y["Gender"])
    


