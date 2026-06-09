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
        print("Rate Movie Selected")

    elif choice == "5":
        print("View Top Rated Movies Selected")

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid Choice!")