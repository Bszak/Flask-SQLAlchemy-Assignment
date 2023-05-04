class MovieRepository:

        def __init__(self, db_url):
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all_movies(self):
        # TODO get all movies from the DB

        return self.session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return self.session.query(Movie).get(movie_id)

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie = Movie(title=title, director=director, rating=rating)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        query = self.session.query(Movie).filter(Movie.title.ilike(f'%{title}%'))
        return query.all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
