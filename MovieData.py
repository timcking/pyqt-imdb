import imdb

class MovieData():
    # Create the object that will be used to access the IMDb's database.
    # By default access the web.
    ia = imdb.IMDb()

    def __init__(self):
        pass

    def get_movie_data(self, movie_id):
        return self.ia.get_movie(movie_id)

    def search_movie_data (self, title):
        return self.ia.search_movie(title)

    def search_movie_data_one (self, title):
        return self.ia.search_movie(title, results=1)

    def get_person_data(self, person_id):
        return self.ia.get_person(person_id)

    def search_person_data(self, name):
        return self.ia.search_person(name)

    def search_person_data_one(self, name):
        return self.ia.search_person(name, results=1)

    def update_movie_data(self, movie):
        self.ia.update(movie)