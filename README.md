# Python-Postgresql-Random-User-Database-
Python script for filling in pSQL database with random Names, Surnames, Usernames, Emails etc..

db_create.sql file is for creating tables in database (3 tables)
Python scripts connect to database and execute commands, also they use 860~ names and 3000~ surnames from wikipedia for creating random people credentials for database.

names.py and surname.py are containing just strings of data

These 3 scripts fill in each table that is created
students.py
professors.py
grades.py 
(Also if you use over 1000 useres there is a chance to repeat username/email which is UNIQUE in table, on 1 milion students i got 18% repeats)

And script averagegrade.py adds in students database average grade for each student.
