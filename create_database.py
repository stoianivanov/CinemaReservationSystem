import sqlite3


db = sqlite3.connect("cinema_data.db")
cursor = db.cursor()

# Create tables
create_movies_table = """
CREATE TABLE IF NOT EXISTS
Movies(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER)
"""
cursor.execute(create_movies_table)

create_projections_table = """
CREATE TABLE IF NOT EXISTS
Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT,
date TEXT, time TEXT,
FOREIGN KEY (movie_id) REFERENCES Movies(id))
"""
cursor.execute(create_projections_table)

create_reservations_table = """
CREATE TABLE IF NOT EXISTS
Reservations(id INTEGER PRIMARY KEY, username TEXT,
projection_id INTEGER, row INTEGER, col INTEGER,
FOREIGN KEY (projection_id) REFERENCES Projections(id))
"""
cursor.execute(create_reservations_table)
db.commit()
