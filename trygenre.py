import json
dict2=[

   {

    "movie_genre":{
       
       "genre1": "Comedy",
        "genre2":"Thriller",
        "genre3": "Action",
        "genre4":"Horror",
        "genre5": "Animation",
        "genre6":"Romance"
        
    }
   }
]
genre=open("genre.json","w")
json.dump(dict2, genre, indent = 6)
genre.close() 