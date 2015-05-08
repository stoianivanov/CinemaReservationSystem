import sqlite3


db = sqlite3.connect("cinema_data.db")
cursor = db.cursor()


def take_available_seats():
    seats = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]
    take_row_col = """
    SELECT row, col FROM Projections
    """
    info = cursor.execute(take_row_col)

    for row in info:
        seats_row = row['row']
        seats_col = row['col']
        seats[seats_row][seats_col] = 'X'

    print("  1 2 3 4 5 6 7 8 9")
    for i in range(0, 11):
        print (i + " ")
        for j in range(0, 11):
            print (j + ' ')
            print(seats[i][j] + ' ')


def make_reservation():
    username = input("Step 1 (User): Choose name>")
    number_of_tickets = input("Step 1 (User): Choose number of tickets>")

    print (" Current movies:")
    show_movies()

    movie_id = input("Step 2 (Movie): Choose a movie>")
    #show_movies_projections

    jection_id = input("Step 3 (Projection): Choose a projection>")
