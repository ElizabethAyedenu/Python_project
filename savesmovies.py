import json

userlist={}
savemovies=[]
# open customer.json file and read it
# def custom():
    
#     # print(customer)
#     detail()


# Ask for the customer email and use it as their username
def detail():
    customerlist=open("try.json","r")
    customer=json.load(customerlist)
     
    username=input("enter your email address: ")

    
# i used for(i.e looping), before writing my conditional ststement because i am trying to access a dictionary
    for y in customer:
        # print(y)
        if y["Email"]==username:
           
            age=y["Age"]
            gender=y["Gender"]
            movie(username,age,gender)
            
        # elif y["Email"] != username:
        #     print("sorry! we don,'t have your details on our database,please enter your correct details")
            

# open the genre.json file and read it
def movie(username,age,gender):
    genrelist=open("genre.json","r")
    genre=json.load(genrelist)
    # print(genre)


#  ask the user to enter 3 differnt movie genre of their choice

    Genre=input("select a movie genre number:Comedy, Thriller,  Action,  Horror,  Animation, Romance: ")
    # Genre2=input("select a movie genre number:Comedy, Thriller, Action, Horror, Animation, Romance: ")
    # Genre3=input("select a movie genre number:Comedy, Thriller, Action, Horror, Animation, Romance: ")
    print(username,",",age,",",gender,", likes",Genre)
    # print(username,",",age,",",gender,", likes",Genre1,",",Genre2,",",Genre3)
   

# enter the details into the empty dictionary
 
    userlist={
        "Username":username,
        "Age":age,
        "Gender":gender,
        "genre":Genre,
        # "genre2":Genre2,
        # "genre3":Genre3
        
    }
    # print(userlist)

# Append the dictionary into an empty array

    savemovies.append(userlist)
    # print(savemovies)
    # for w in savemovies:
    #     if len(savemovies)==5:


# copy the details and save the persons details into a json file

    list=open("savemovies.json","w")
    json.dump(savemovies,list,indent=4)
    list.close()
def yeye():
    
    detail()
    
    if len(savemovies)==2:
            print("we don finish")
    else:
        yeye()

yeye()
        
    
        
    # movie2(username,genre,Genre,savemovies)
    # movie2(username,genre,Genre1,Genre2,Genre3,savemovies)
    
# def movie2(username,genre,Genre1,savemovies):    
#     point=0
#     movies=savemovies
# i did not use a "for" statement here because i am trying to access an array or list.i used a direct conditional statement 

    # if Genre1==genre[0]:
    #     point+=1
    # if Genre1==genre[1]:
    #     point+=1
    # if Genre1==genre[2]:
    #     point+=1
    # if Genre1==genre[3]:
    #     point+=1
    # if Genre1==genre[4]:
    #     point+=1
    # if Genre1==genre[5]:
    #     point+=1

    # if Genre2==genre[0]:
    #     point+=1
    # if Genre2==genre[1]:
    #     point+=1
    # if Genre2==genre[2]:
    #     point+=1
    # if Genre2==genre[3]:
    #     point+=1
    # if Genre2==genre[4]:
    #     point+=1
    # if Genre2==genre[5]:
    #     point+=1

    # if Genre3==genre[0]:
    #     point+=1
    # if Genre3==genre[1]:
    #     point+=1
    # if Genre3==genre[2]:
    #     point+=1
    # if Genre3==genre[3]:
    #     point+=1
    # if Genre3==genre[4]:
    #     point+=1
    # if Genre3==genre[5]:
    #     point+=1
    # print("The movie point for",username,"is",point)
#     yeye()

                            
# def yeye():
#     custom()
#     detail()
#     movie()
#     movie2()
       
   

    # if len(movies)==5:
    #         print("we don finish")
    # else:
    #     yeye(movies)
