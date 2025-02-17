import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ufM4ddY!lopnhes",
    database="movies"  # Directly specifying the database name
)

cursor = conn.cursor()

# Query 1: Select all fields from the studio table
print("DISPLAYING Studio RECORDS")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}\n")

# Query 2: Select all fields from the genre table
print("DISPLAYING Genre RECORDS")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}\n")


# Query 3: Select movie names with runtime less than 2 hours
print("DISPLAYING Short Movie RECORDS")
cursor.execute("SELECT film_name, runtime  FROM short_films WHERE runtime < 120")
short_movies = cursor.fetchall()
for movie in short_movies:
    print("Film Name: {}\n Runtime:{}\n".format(movie[0], movie[1]))

    
 

# Query 4: Select film names and directors
print("DISPLAYING Director and Films")
cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
director_movies = cursor.fetchall()
for movie in director_movies:
    print("Director: {}\n Film Name:{}\n".format(movie[0], movie[1]))

# Close connection
    cursor.close()
    conn.close()
