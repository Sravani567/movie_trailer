import webbrowser
class movie():
    def __init__(self,name_of_the_movie,story_line,movie_poster,movie_trailer_youtube):
        self.name=name_of_the_movie
        self.storyline=story_line
        self.poster_url=movie_poster
        self.trailer_youtube_url=movie_trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
