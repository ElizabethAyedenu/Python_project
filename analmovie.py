import json
analyse=open("savemovies.json","r")
saved_movies=json.load(analyse)
analyse.close()
analyse=[]
print(saved_movies)
for x in range(len(saved_movies)):
    
    
    analyse.append(saved_movies[x]["genre"])
    print(analyse)
    a=analyse.count("Comedy")
    b=analyse.count("Thriller")
    c=analyse.count("Action")
    d=analyse.count("Animation")
    e=analyse.count("Romance")
    f=analyse.count("Horror")
    print("comedy has",a,"views.\n""thriller has",b,"views. \n""action has",c,"views.\n""animation has",d,"views.\n" "romance has",e,"views.\n""horror has",f,"views.\n")






    