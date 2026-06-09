import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
SELECT movie_id,
       title,
       genre_id,
       release_year
FROM movies
""")

for row in cursor.fetchall():
    print(row)

conn.close()