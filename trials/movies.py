from tmdbv3api import TMDb, Movie

tmdb = TMDb();

tmdb.api_key = "88e01c9c6c65ce312ee50a4358e089ac"

tmdb.language = "en"
tmdb.debug = True

movie = Movie()

print(movie.details(268).encode("utf-8") )

