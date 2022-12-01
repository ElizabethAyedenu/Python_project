import json

# def customer_list():

    out_file = open ("customer.json","r")
    customer=json.load(out_file)
    print(customer)
#     genre_list()
#     savedmovies(customer)

# def genre_list():
genre=open("genre.json","r")
Genre=json.load(genre)
print(Genre)
        
user_id=[]
savedmovies=[]

def userid():



    email=(input("please enter your email: "))
    user_id.append(email)
    if len(user_id) == 2:
        function2()
        
    else:
         userid()
def function2():
    genre=input("enter your genre of movie: ")
    savedmovies.append(genre)
    if len(savedmovies)>= 3:
        print(savedmovies)
    else:
        function2()
user_id()