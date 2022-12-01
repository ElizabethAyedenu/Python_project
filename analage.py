import json
analyse=open("savemovies.json","r")
saved_movies=json.load(analyse)
for x in saved_movies:
    age=[]
    print(x["Age"])
    if x["Age"]<=18:
        print(x["Username"],"is within 18-25 age range")
        age.append(x["Age"])
    # elif x["Age"]>=25:
    #     print(x["Username"],"is within 18-25 age range")
    elif x["Age"]<=26:
        print(x["Username"],"is within 26-30 age range")
        age.append(x["Age"])
    # elif x["Age"]>=30:
    #     print(x["Username"],"is within 26-30 age range")
    elif x["Age"]<=40:
        print(x["Username"],"is within 40-50 age range")
        age.append(x["Age"])
    # elif x["Age"]>=50:
    #     print(x["Username"],"is within 40-50 age range")
    
    elif x["Age"]>=60:
        print(x["Username"],"is within 60 and above age range")
        age.append(x["Age"])
    else:
        print("your age_range is not in our database")



