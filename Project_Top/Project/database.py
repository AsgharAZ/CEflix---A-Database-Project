import pyodbc

def connect_db():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-VO1PBUT\\SQLSERVER;"
        "Database=Project;"
        "Trusted_Connection=yes;"
    )

def authenticate_user(username, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT Password FROM [User] WHERE User_Name = ? OR User_Email = ?", (username, username))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user and user[0] == password

def authenticate_admin(username, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT Password FROM [Admin] WHERE Admin_Name = ? OR Admin_Email = ?", (username, username))
    admin = cursor.fetchone()
    cursor.close()
    connection.close()
    return admin and admin[0] == password

def register_user(username, email, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO [User] (User_Name, User_Email, Password, Date_Of_Creation) VALUES (?, ?, ?, ?)",
                   (username, email, password, '2024-11-16'))  # Replace with current date
    connection.commit()
    cursor.close()
    connection.close()

def register_admin(username, email, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO [Admin] (Admin_Name, Admin_Email, Password, Date_Of_Creation) VALUES (?, ?, ?, ?)",
                   (username, email, password, '2024-11-16'))  # Replace with current date
    connection.commit()
    cursor.close()
    connection.close()

def add_movie(movie_name, genre, summary, year, duration, crew, admin_id):
    # Establish database connection
    connection = connect_db()
    cursor = connection.cursor()

    # Insert the movie details into the Movie table
    cursor.execute("""
    INSERT INTO Movie (Movie_Name, Summary, Year, Admin_ID, Duration)
    VALUES (?, ?, ?, ?, ?)
    """, (movie_name, summary, year, admin_id, duration))

    # Commit the transaction for Movie table insertion
    connection.commit()
    print("Movie insertion committed")

    # Retrieve the Movie_ID using Movie_Name (and other attributes)
    cursor.execute("""
    SELECT Movie_ID FROM Movie
    WHERE Movie_Name = ? AND Summary = ? AND Year = ? AND Duration = ?
    """, (movie_name, summary, year, duration))

    # Fetch the Movie_ID
    result = cursor.fetchone()

    if result is None:
        print("Error: Movie_ID could not be retrieved.")
        connection.close()
        return

    movie_id = result[0]
    print(f"Retrieved Movie_ID: {movie_id}")

    # Set IDENTITY_INSERT to ON for the Genre table
    cursor.execute("SET IDENTITY_INSERT Genre ON")
    
    # Split and insert genre data into Genre table
    genre_list = [g.strip() for g in genre.split(",")]  # Split genres by comma and trim whitespace
    for g in genre_list:
        cursor.execute("""
        INSERT INTO Genre (Movie_ID, Genre)
        VALUES (?, ?)
        """, (movie_id, g))

    # Set IDENTITY_INSERT to OFF for the Genre table
    cursor.execute("SET IDENTITY_INSERT Genre OFF")

    # Set IDENTITY_INSERT to ON for the Crew table
    cursor.execute("SET IDENTITY_INSERT Crew ON")
    
    # Split and insert crew data into Crew table
    crew_list = [c.strip() for c in crew.split(",")]  # Split crew members by comma and trim whitespace
    for c in crew_list:
        cursor.execute("""
        INSERT INTO Crew (Movie_ID, Cast)
        VALUES (?, ?)
        """, (movie_id, c))

    # Set IDENTITY_INSERT to OFF for the Crew table
    cursor.execute("SET IDENTITY_INSERT Crew OFF")

    # Commit all transactions
    connection.commit()
    print("All data committed")

    # Close the cursor and connection
    cursor.close()
    connection.close()
