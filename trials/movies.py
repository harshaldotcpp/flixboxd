from tmdbv3api import TMDb, Movie

tmdb = TMDb();

tmdb.api_key = "88e01c9c6c65ce312ee50a4358e089ac"

tmdb.language = "en"
tmdb.debug = True

movies = Movie()

search = movies.search("the batman")

movie_id  = 0

for res in search:
    if(res["original_title"] =="The Batman"):
        movie_id = res.id


movie_dir = movies.credits(movie_id)

for i in movie_dir.crew:
    if(i["job"] == "Director"):
        print(i)
