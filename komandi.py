from prettytable import PrettyTable


print("You can use the following commands:\nshow_movies\n\
show_movie_projections <movie_id> [<date>]\nmake_reservation\n\
cancel_reservation <name>\nexit\nhelp")
command = input("command> :")


def show_movies():
    pass


def show_movie_projections(movie_id, date=None):
    pass


def make_reservation():
    pass


def cancel_reservation(name):
    pass


def exit():
    pass


def helpp():
    pass


def main():
    pass

commands = {
           "show_movies": show_movies,
           "show_movie_projections": show_movie_projections,
           "make_reservation": make_reservation,
           "cancel_reservation": cancel_reservation,
           "exit": exit,
           "help": helpp
           }

if __name__ == '__main__':
    main()
