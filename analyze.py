import json
analyse=open("savemovies.json","r")
saved_movies=json.load(analyse)
analyse.close()

print(len(saved_movies))
point=0
point1=0
point2=0
point3=0
point4=0
point5=0
for x in range(len(saved_movies)):
    # print (saved_movies[x])
    if saved_movies[x]["genre"]=="Comedy":
        point+=1
        # print("comedy point")
    elif saved_movies[x]["genre"]=="Thriller":
        point1+=1
        # print("thriller point")
    elif saved_movies[x]["genre"]=="Action":
        point2+=1
        # print("action point")
    elif saved_movies[x]["genre"]=="Horror":
        point3+=1
        # print("horror point")
    elif saved_movies[x]["genre"]=="Animation":
        point4+=1
        # print("animation point")
    elif saved_movies[x]["genre"]=="Romance":
        point5+=1
        # print("romance point")

   
# print(max(point,point1,point2,point3,point4,point5))
print("comedy appears:",point,"times.",
"thriller appears:",point1,"times.",
"action appears:",point2,"times.",
"horror appears:",point3,"times.",
"animmation appears:",point4,"times.",
"romance appears:",point5,"times.")

    # print(x.values())
    
    # print "Comedy" in banji.values() :
    #     point+=1
    #     print("comedy point =",point)
    # elif "Thriller"in x.values() :
    #     point1+=1
    #     print("thriller point =",point1)
    # elif x.value() == "Action":
    #     point2+=1
    #     print("action point =",point2)
    # elif x.value() == "Animation":
    #     point3+=1
    #     print("animation point =",point3)
    # elif x.value() == "Romance":
    #     point4+=1
    #     print("thriller point =",point4)
    # elif x.value() == "Horror":
    #     point5+=1
    #     print("thriller point =",point5)
    

# print(analyse_list)

# genrelist=open("genre.json","r")
# genre=json.load(genrelist)
# # print(genre)

# customerlist=open("try.json","r")
# customer=json.load(customerlist)
# print(customer)
# age_range1="18-15"
# age_range2="26-30"
# age_range3="40-50"
# age_range4="60"
# for x in saved_movies:
#     if x["Age"]<=18: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
    
#     elif x["Age"]<=26: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
    
#     elif x["Age"]<=40: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
       
#     elif x["Age"]>=60: 
#         print(x["Username"]," of",x["Age"],"years of Age likes",x["genre"]["genre1"],",",x["genre"]["genre2"],",",x["genre"]["genre3"])
#     else:
         
#         print("sorry",x["Username"]," of",x["Age"],"years of Age you are not in our age range")
    
    
# genre[0]="Comedy"
# genre[1]="Thriller"
# genre[2]="Action"
# genre[3]="Horror"
# genre[4]="Animation"
# genre[5]="Romance"

# def funny():
#     for x in saved_movies:
#         for y in customer:
            
#                 if x["Username"]==y["Email"]:
#                     print(x["Username"])
#                 operation(x)
# def operation(x):
#     point=0
#     if x["genre"]["genre1"]==genre[0]:
#         print("true1")
#     if x["genre"]["genre2"]==genre[0]:
#         point+=1
#         print("true2")
#     if x["genre"]["genre3"]==genre[0]:
#         print("true3")
#         point+=1

#     if x["genre"]["genre1"]==genre[1]:
#         print("true4")
#         point+=1
#     if x["genre"]["genre2"]==genre[1]:
#         print("true5")
#         point+=1
#     if x["genre"]["genre3"]==genre[1]:
#         print("true6")
#         point+=1
    
#     if x["genre"]["genre1"]==genre[2]:
#         print("true7")
#         point+=1
#     if x["genre"]["genre2"]==genre[2]:
#         print("true8")
#         point+=1
#     if x["genre"]["genre3"]==genre[2]:
#         point+=1
#         print("true9")
    
#     if x["genre"]["genre1"]==genre[3]:
#         point+=1
#         print("true0")
#     if x["genre"]["genre2"]==genre[3]:
#         point+=1
#         print("true11")
#     if x["genre"]["genre3"]==genre[3]:
#         print("true12")
#         point+=1

#     if x["genre"]["genre1"]==genre[4]:
#         point+=1
#         print("true13")
#     if x["genre"]["genre2"]==genre[4]:
#         print("true14")
#         point+=1
#     if x["genre"]["genre3"]==genre[4]:
#         point+=1
#         print("true15")
    
#     if x["genre"]["genre1"]==genre[5]:
#         print("true16")
#         point+=1
#     if x["genre"]["genre2"]==genre[5]:
#         print("true17")
#         point+=1
#     if x["genre"]["genre3"]==genre[5]:
#         point+=1
#         print("true18")
#     # print(point)
    
    


# funny()
        
            
    

        # print(x["genre"]["genre1"])
        # print(y) 