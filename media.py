import webbrowser

'''This class provides a way to store movie related info'''


class Movie():

	'''Intiate objects'''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''open a web page that plays trailer on youtube'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    '''open a web page that shows poster of the movie'''
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    '''print out the title of the movie'''
    def show_title(self):
        print(self.title)

    '''print out the storyline of the movie'''
    def show_storyline(self):
        print(self.storyline)
