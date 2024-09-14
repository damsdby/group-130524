import sqlite3
import hashlib
from pprint import pprint

DB_PATH = 'our_db_13052024.sqlite3'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS school(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            number VARCHAR(20) NOT NULL,
            
            address TEXT,
            number_of_floors INTEGER CHECK (number_of_floors > 1)
        )
    """
    cursor.execute(query)

    query_students = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT NOT NULL ,
        name TEXT NOT NULL ,
        specialization TEXT NOT NULL,
        school_id INTEGER,
        FOREIGN KEY (school_id) REFERENCES school(id)
    );
    """

    query = """
        INSERT INTO school (number, address, number_of_floors)
        VALUES ('School 1', 'Haar', 3);
        """
    cursor.execute(query)

    query = """
        INSERT INTO students (surname, name, specialization, school_id)
        VALUES ('Ivanov', 'Ivan', 'Mathematics', 1);
        """
    cursor.execute(query)

    schools = [
        ('School 2', 'Zentrum', 2),
        ('School 3', 'Pine', 4),
        ('School 4', 'Levoberezhnaya', 5)
    ]
    cursor.executemany("""
        INSERT INTO school (number, address, number_of_floors)
        VALUES (?, ?, ?);
        """, schools)

    students = [
        ('Yan', 'Petr', 'Physics', 1),
        ('Jon', 'Jones', 'Sport', 2),
        ('Conor', 'Mackregor', 'Chemistry', 2),
        ('Habib', 'Nurmagomedov', 'Dagestanologia', 1),
        ('Usman', 'Saburov', 'Dagestanologia', 3),
        ('Fedor', 'Emelyaninko', 'Physics', 3),
        ('Zhukov', 'Nikolay', 'Geography', 4),
        ('Sokolova', 'Elena', 'Biology', 4),
        ('Lebedev', 'Sasha', 'History', 4),
        ('Kuzmin', 'Viktor', 'Mathematics', 3)
    ]

    cursor.executemany("""
               INSERT INTO students (surname, name, specialization, school_id)
               VALUES (?, ?, ?, ?);
               """, students)
