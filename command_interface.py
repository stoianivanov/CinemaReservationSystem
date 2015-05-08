import sqlite3


db = sqlite3.connect("cinema_data.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def take_available_seats():
    seats = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]
    take_row_col = """
    SELECT row, col FROM Reservations
    """
    info = cursor.execute(take_row_col)

    for row in info:
        seats_row = row['row']
        seats_col = row['col']
        seats[seats_row][seats_col] = 'X'

    print("  1    2    3    4    5    6    7    8    9    10")
    for i in range(0, len(seats)):
        print(seats[i])


def take_seat(username, projection_id, row, col):
    take_row_col = """
    SELECT row, col FROM Reservations
    """
    info = cursor.execute(take_row_col)

    for line in info:
        seats_row = line['row']
        seats_col = line['col']
        if row == seats_row and col == seats_col:
            print ('Lol...NO!')
            return False

    cursor.execute("""
    INSERT INTO Reservations(username, projection_id, row, col)
    VALUES(?, ?, ?, ?)
    """, (username, str(projection_id), str(row), str(col)))
    db.commit()
    return True


def choose_seat(username, projection_id, number):
    counter = 1
    seats = []
    while number > 0:
        print ('Step 4 (Seats): Choose seat {}>'. format(counter))
        row = int(input()) - 1
        col = int(input()) - 1
        if take_seat(username, projection_id, row, col):
            number -= 1
            counter += 1
            seats.append((row, col))
    else:
        info = cursor.execute("""
        SELECT projection_type, projection_date, projection_time,
        movie_name, movie_rating
        FROM Projections
        JOIN Movies
        ON Projections.movie_id = Movies.id
        WHERE Projections.id = ?
        """, str(projection_id))
        db.commit()
        for row in info:
            print ('This is your reservation:')
            print ('Movie: {} ({})'.format(row['movie_name'],row['movie_rating']))
            print ('Date and Time: {} ({})'.format(row['projection_date'], row['projection_type']))
            print ('Seats: {}'. format(seats))


take_available_seats()
choose_seat("pesho", 2, 4)
take_available_seats()


def make_reservation():
    username = input("Step 1 (User): Choose name>")
    number_of_tickets = input("Step 1 (User): Choose number of tickets>")

    print (" Current movies:")
    show_movies()

    movie_id = input("Step 2 (Movie): Choose a movie>")
    show_movies_projections(movie_id)

    projection_id = input("Step 3 (Projection): Choose a projection>")
    take_available_seats()

    choose_seat(username, projection_id, number_of_tickets)
