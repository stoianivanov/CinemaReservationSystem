import sqlite3
from prettytable import PrettyTable

db = sqlite3.connect("cinema_data.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def show_movies():
    table = PrettyTable(["ID", "Title", "Rating"])
    info = cursor.execute("SELECT id, movie_name, movie_rating FROM Movies")
    for row in info:
        table.add_row([row["id"], row["movie_name"], row["movie_rating"]])
    print("Current movies:\n")
    print(table)
    main()


def show_movie_projections(movie_id, date=None):
    printed = False
    table = PrettyTable(["ID", "Date", "Starting_hour", "Type"])
    info = cursor.execute("""SELECT Projections.id, projection_type,
                                    projection_date, projection_time,
                                    movie_id, movie_name
                             FROM Projections
                             JOIN Movies
                             ON Projections.movie_id = Movies.id
                             WHERE movie_id = ?""", str(movie_id))
    for row in info:
        if not printed:
            print("Projections for movie '{}':".format(row["movie_name"]))
            printed = True
        table.add_row([row["id"], row["projection_date"],
                      row["projection_time"], row["projection_type"]])
    print(table)
    main()


def make_reservation():
    pass


def cancel_reservation(name):
    cursor.execute("DELETE FROM Reservations WHERE username = ?", (name, ))
    db.commit()
    main()


def exit():
    pass


def commands_help():
    print("You can use the following commands:\nshow_movies\n\
show_movie_projections <movie_id> [<date>]\nmake_reservation\n\
cancel_reservation <name>\nexit\nhelp")
    main()


def main():
    command = input("command>: ")
    try:
        command1 = command.split()[0]
        command2 = command.split()[1]
    except:
        pass
    if command1 not in commands:
        print("Your command is not valid.\n\
Try using <help> to see all the available commadns.")
        main()
    else:
        try:
            commands[command1](command2)
        except:
            commands[command1]()

commands = {
           "show_movies": show_movies,
           "show_movie_projections": show_movie_projections,
           "make_reservation": make_reservation,
           "cancel_reservation": cancel_reservation,
           "exit": exit,
           "help": commands_help
           }

if __name__ == '__main__':
    main()
