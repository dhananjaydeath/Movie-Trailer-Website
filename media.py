import webbrowser


# Movie class is defined over here
class Movie():
	# __init__ constructor of Movie class is defined,
	# it initializes the objects of movie class with relevant details
	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
