import json
user_id=""
customer_list=[]
def signup():
    global customer_list
    global user_id
    mydict={}
    Name=input("please enter your first name: ")
    mydict["Age"]=int(input("enter your age: "))
    mydict["Gender"]=input("what is your gender? male or female")
    mydict["Email"]=input("enter your email address")
    mydict["Password"]=input("enter your password")
    genre=("movie_genre")
    mydict[genre]={}
    genreA=input("please enter a preferred movie genre you enjoy: ")
    genreB=input("please enter a preferred movie genre you enjoy: ")
    genreC=input("please enter a preferred movie genre you enjoy: ")
    mydict[genre]["genreA"]=genreA
    mydict[genre]["genreB"]=genreB
    mydict[genre]["genreC"]=genreC
    user_id=mydict["Email"]
    print(user_id)
    outfile(mydict)
def outfile(mydict):
    for x in range(2):
        out_file = open ("try.json","w")
        json.dump(mydict, out_file, indent = 6)
        out_file.close()    
    

        
# def movielist(mydict):    
#     for x in mydict:
#         if 

signup()

