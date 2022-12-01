import json
dict1=[
    {
    "user1":{
        "name":input("please enter your first name: "),
        "name2":input("please enter  your last name: "),
        "age":int(input("enter your age: ")),
        "gender":input("what is your gender? male or female? : "),
        "email": input("enter your email: "),
        "password":input("enter your desired password: "),
        
        
    },
    "user2":{
       "name":input("please enter your name: "),
       "name2":input("please enter  your last name: "),
        "age":int(input("enter your age: ")),
        "gender":input("what is your gender? male or female? : "),
        "email": input("enter your email: "),
        "password":input("enter your desired password: "),
        
    },
    "user3":{
       "name":input("please enter your name: "),
       "name2":input("please enter  your last name: "),
        "age":int(input("enter your age: ")),
        "gender":input("what is your gender? male or female? : "),
        "email": input("enter your email: "),
        "password":input("enter your desired password: "),
        
    },
    "user4":{
       "name":input("please enter your name: "),
       "name2":input("please enter  your last name: "),
        "age":int(input("enter your age: ")),
        "gender":input("what is your gender? male or female? : "),
        "email": input("enter your email: "),
        "password":input("enter your desired password: "),
        
    },
    "user5":{
       "name":input("please enter your name: "),
       "name2":input("please enter  your last name: "),
        "age":int(input("enter your age: ")),
        "gender":input("what is your gender? male or female? : "),
        "email": input("enter your email: "),
        "password":input("enter your desired password: "),
        
    }
    }
]
out_file = open ("customer.json","w")
json.dump(dict1, out_file, indent = 6)
out_file.close()