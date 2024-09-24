"""db.py: connect to Postgres database and create tables"""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from db.sql import queries

# import environment variables from .env
load_dotenv()

db_name: str = os.getenv('db_name')
db_owner: str = os.getenv('db_owner')
db_pass: str = os.getenv('db_pass')
db_uri: str = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

# create the flask application & connect to db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)

# this import is here because we need to initialize db before importing it into
# the classes
from db.schema.assoc import ProfessorCourse
from db.schema.course import Course
from db.schema.professor import Professor

# verify the db connection is successful
with app.app_context():
    # attempt to connect to db, print msgs if successful
    try:
        # run SQL query to verify connection (see how we use the db instance?)
        db.session.execute(text("SELECT 1"))
        print(f"\n\n----------- Connection successful!")
        print(f" * Connected to database: {os.getenv('db_name')}")
    # failed to connect to db, provide msgs & error
    except Exception as error:
        print(f"\n\n----------- Connection failed!")
        print(f" * Unable to connect to database: {os.getenv('db_name')}")
        print(f" * ERROR: {error}")
    
    # create all database tables
    db.create_all()

    # run queries to remove data from tables
    for key, value in queries.items():
        db.session.execute(text(value))
        db.session.commit()
    

    # LAB 4 --------------------------------------------------

    # Write a query to insert 3 records into the Courses table
    # Query 1
    query_1 = """
    INSERT INTO "Courses" ("CourseID", "CourseName", "Semester", "Year")
    VALUES 
        (101, 'MATH', 'FALL', 2024),
        (102, 'PROGRAMMING', 'SPRING', 2025),
        (103, 'HISTORY', 'FALL', 2024),
        (104, 'BIOLOGY', 'SPRING', 2025);
    """
    db.session.execute(text(query_1))
    db.session.commit()

    # Write a query to select all records from the Courses table
    # Query 2
    query_2 = """SELECT * FROM "Courses" """
    courses = db.session.execute(text(query_2))
    print("\n\n----------- Courses Table")
    for course in courses:
        print(course)

    # Write a query to update 1 record in the Courses table
    # Query 3
    query_3 = """
    UPDATE "Courses"
    SET "CourseName" = 'CALCULUS'
    WHERE "CourseID" = 101
    """
    db.session.execute(text(query_3))
    db.session.commit()

    # Write a query to delete 1 record in the Courses table
    # Query 4
    query_4 = """
    DELETE FROM "Courses"
    WHERE "CourseID" = 103
    """
    db.session.execute(text(query_4))
    db.session.commit()

    # Print data to terminal
    print("\n\n----------- Courses Table")
    courses = db.session.execute(text(query_2))
    for course in courses:
        print(course)
