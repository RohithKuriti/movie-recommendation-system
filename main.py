import sqlite3

def add_genre():
    genre_name = input("Enter Genre Name: ")

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO genres (genre_name) VALUES (?)",
        (genre_name,)
    )

    conn.commit()
    conn.close()

    print("Genre Added Successfully!")
def add_movie():
    title = input("Enter Movie Title: ")

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    print("\nAvailable Genres:")

    cursor.execute("SELECT * FROM genres")

    genres = cursor.fetchall()

    for genre in genres:
        print(genre)

    genre_id = int(input("Enter Genre ID: "))
    release_year = int(input("Enter Release Year: "))

    cursor.execute(
        """
        INSERT INTO movies(title, genre_id, release_year)
        VALUES(?, ?, ?)
        """,
        (title, genre_id, release_year)
    )

    conn.commit()
    conn.close()

    print("Movie Added Successfully!")
def register_user():
    username = input("Enter Username: ")

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username) VALUES(?)",
        (username,)
    )

    conn.commit()
    conn.close()

    print("User Registered Successfully!")
def rate_movie():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    print("\nUsers:")
    cursor.execute("SELECT * FROM users")
    for user in cursor.fetchall():
        print(user)

    user_id = int(input("Enter User ID: "))

    print("\nMovies:")
    cursor.execute("SELECT * FROM movies")
    for movie in cursor.fetchall():
        print(movie)

    movie_id = int(input("Enter Movie ID: "))

    rating = int(input("Enter Rating (1-5): "))
    review = input("Enter Review: ")

    cursor.execute(
        """
        INSERT INTO ratings(user_id, movie_id, rating, review)
        VALUES(?, ?, ?, ?)
        """,
        (user_id, movie_id, rating, review)
    )

    conn.commit()
    conn.close()

    print("Rating Added Successfully!")
def view_top_rated_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT m.title,
               AVG(r.rating) as avg_rating
        FROM movies m
        JOIN ratings r
        ON m.movie_id = r.movie_id
        GROUP BY m.movie_id
        ORDER BY avg_rating DESC
    """)

    results = cursor.fetchall()

    print("\n===== Top Rated Movies =====")

    for movie in results:
        print(f"{movie[0]} -> {movie[1]:.2f}")

    conn.close()

while True:
    print("\n===== Movie Recommendation System =====")
    print("1. Add Genre")
    print("2. Add Movie")
    print("3. Register User")
    print("4. Rate Movie")
    print("5. View Top Rated Movies")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_genre()

    elif choice == "2":
        add_movie()

    elif choice == "3":
        register_user()

    elif choice == "4":
        rate_movie()

    elif choice == "5":
        view_top_rated_movies()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid Choice!")