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
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(Movie_ID) FROM Movies")
    movie_id = cursor.fetchone()[0] + 1 if cursor.fetchone()[0] else 1

    cursor.execute("""
    INSERT INTO Movies (Movie_ID, Movie_Name, Summary, Year, Duration, Crew, Admin_ID)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (movie_id, movie_name, summary, year, duration, crew, admin_id))

    connection.commit()
    cursor.close()
    connection.close()