import media
import fresh_tomatoes

# create instance of movies in which it contains title, storyline, poster img, and a youtube trailer 
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					"A soldier on an alien planet",
					"http://avatarblog.typepad.com/.a/6a0120a6b2c140970c012876c79e1a970c-800wi",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")


wallflower = media.Movie("The Perks of Being a Wallflower",
						"An introvert freshman is taken under the wings of two seniors who welcome him to the real world.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMzIxOTQyODU1OV5BMl5BanBnXkFtZTcwMDQ4Mjg4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=2vb2qrcPEEs")

blue = media.Movie("Blue is the Warmest Color",
					"Adele's life is changed when she meets Emma. A broken hearted story",
					"http://img.moviepostershop.com/blue-is-the-warmest-color-movie-poster-2013-1010768647.jpg",
					"https://www.youtube.com/watch?v=Y2OLRrocn3s")

lalaland = media.Movie("La La Land",
						"Two proper L.A. dreamers, a suavely charming soft-spoken jazz pianist and a brilliant vivacious playwright, while waiting for their big break, attempt to reconcile aspirations and relationship in a magical old-school romance.",
						"https://theofficela.files.wordpress.com/2017/01/la-la-land-2016-movie-poster.jpg",
						"https://www.youtube.com/watch?v=0pdqf4P9MB8")

horrible_bosses = media.Movie("Horrible Bosses",
							"Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness",
							"https://resizing.flixster.com/1PX_qcRl9z_rzg81gPZuEdszyO4=/300x300/v1.bTsxMTE2MzY3MztqOzE3NDU0OzEyMDA7NjQwOzk2MA",
							"https://www.youtube.com/watch?v=YnzIA-yu268")

# create a list of movies
movies = [toy_story, avatar, wallflower, blue, lalaland, horrible_bosses]

# generate html page by calling fresh_tomatoes open movies page function
fresh_tomatoes.open_movies_page(movies)