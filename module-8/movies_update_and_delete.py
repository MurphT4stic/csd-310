import mysql.connector
def show_films(cursor,title):

    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id") 

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {} \nGenre Name ID: {}\nStudio Name: {}\n".format (film[0], film[1], film[2], film[3])) 


# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ufM4ddY!lopnhes",
    database="movies"  # Directly specifying the database name
)

cursor = conn.cursor()
show_films(cursor, "DISPLAYING FILMS")

#query= "insert into film(film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) values (4, 'Transformers', '2007', 150, 'Micheal Bay', 3, 2)"
#cursor.execute(query) 
#conn.commit() 
show_films(cursor, "DISPLAYING FILMS")
query= "UPDATE film set genre_id = 2 WHERE film_name = 'Alien'"
cursor.execute(query)
conn.commit()
show_films(cursor, "DISPLAYING FILMS") 
query= "DELETE FROM film WHERE genre_id=3"
cursor.execute(query)
conn.commit() 