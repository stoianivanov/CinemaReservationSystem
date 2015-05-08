import sqlite3
from prettytable import PrettyTable

db = sqlite3.connect("cinema_data.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def show_movies():
    table = PrettyTable(["ID", "Title", "Rating"])
    info = cursor.execute("SELECT id, name, rating FROM Movies")
    for row in info:
        table.add_row([row["id"], row["name"], row["rating"]])
    print("Current movies:\n")
    print(table)


def show_movie_projections(movie_id, date=None):
    pass


def make_reservation():
    pass


def cancel_reservation(name):
    pass


def exit():
    pass


def commands_help():
    print("You can use the following commands:\nshow_movies\n\
show_movie_projections <movie_id> [<date>]\nmake_reservation\n\
cancel_reservation <name>\nexit\nhelp")


def main():
    command = input("command>: ")
    used_command = command.split()[0]
    if used_command not in commands:
        print("Your command is not valid.\n\
Try using <help> to see all the available commadns.")
    else:
        commands[used_command]()

    # user_command = command.split()[0]
    # try:
    #     user_id = command.split()[1]
    #     commands[user_command](user_id)
    #     print("i deleted")
    # except:
    #     commands[user_command]()

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
