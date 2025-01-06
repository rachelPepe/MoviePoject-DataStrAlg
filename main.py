from ChainingHashTable import ChainingHashTable
from Movie import Movie
import csv

def loadMovieData(filename):
    with open(filename) as best_movies:
        movie_data = csv.reader(best_movies, delimiter=',')
        next(movie_data) # skip header
        for movie in movie_data:
            m_ID = int(movie[0])
            m_title = movie[1]
            m_year = movie[2]
            m_price = movie[3]
            m_city = movie[4]
            m_state = movie[5]
            m_status = 'Loaded'

            # movie object
            movie = Movie(m_ID, m_title, m_year, m_price, m_city, m_state, m_status)

            # insert into the hash table
            movie_hash.insert(m_ID, movie)

# hash table instance
movie_hash = ChainingHashTable()

# load movie into hash table
loadMovieData('BestMovies.csv')

# fetch data from hash table

for i in range(len(movie_hash.table) + 1):
    print("Key: {} and Movie: {}".format(i+1, movie_hash.search(i+1)))







