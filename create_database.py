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
date TEXT, time TEXT)
"""
cursor.execute(create_projections_table)

create_reservations_table = """
CREATE TABLE IF NOT EXISTS
Reservations(id INTEGER PRIMARY KEY, username TEXT,
projection_id INTEGER, row INTEGER, col INTEGER)
"""
cursor.execute(create_reservations_table)
db.commit()

# # Insert students
# cursor.executemany(""" INSERT INTO Students(
# student_name,
# student_github) VALUES(?,?)""", hackbg_info.get_student_and_github())
# db.commit()

# # Insert courses
# cursor.executemany(""" INSERT INTO Courses(
# course_name) VALUES(?)""", hackbg_info.get_all_courses())
# db.commit()

# # Create students and courses dicts
# courses_ids_names = cursor.execute(
#     "SELECT course_id, course_name FROM Courses")
# courses_dict = {course[1]: course[0] for course in courses_ids_names}
# db.commit()

# students_ids_names = cursor.execute(
#     "SELECT student_id, student_name FROM Students")
# students_dict = {student[1]: student[0] for student in students_ids_names}
# db.commit()

# # Insert relations
# for student_and_course in hackbg_info.get_student_and_course():
#     for course in student_and_course[1]:
#         cursor.execute(""" INSERT INTO Students_to_courses(
# s_id, c_id) VALUES(?,?)""", (students_dict[student_and_course[0]], courses_dict[course]))
# db.commit()
