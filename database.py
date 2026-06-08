import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS genres(
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre_id INTEGER,
    release_year INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")