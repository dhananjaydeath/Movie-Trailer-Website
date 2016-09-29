import fresh_tomatoes
import media


# creating instances or objects of Movie class and passing movie name,
# movie poster and youtube url of movie as arguments that __init__ method define
mega_mind = media.Movie("Mega Mind",
						"https://upload.wikimedia.org/wikipedia/en/8/89/Megamind2010Poster.jpg",
						"https://www.youtube.com/watch?v=Xu42-p6_5RE")

ratatouille = media.Movie("Ratatouille",
						  "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

big_hero_6 = media.Movie("Big Hero 6",
						 "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
						 "https://www.youtube.com/watch?v=z3biFxZIJOQ")

frozen = media.Movie("Frozen",
					 "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
					 "https://www.youtube.com/watch?v=FLzfXQSPBOg")

tangled = media.Movie("Tangled",
					  "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
					  "https://www.youtube.com/watch?v=wCxuxrLNrsw")

cars = media.Movie("Cars",
				   "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
				   "https://www.youtube.com/watch?v=WGByijP0Leo")

# creating a list of movies file
movies_list = [
	mega_mind, ratatouille, big_hero_6, 
	frozen, tangled, cars
	]

# calling open_movies_page function stored in fresh_tomatoes file and 
# passing the movies_list as arguments in the function
fresh_tomatoes.open_movies_page(movies_list)