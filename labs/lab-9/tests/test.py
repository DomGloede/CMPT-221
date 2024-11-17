import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# Test user signup with valid data
def test_signup_valid_data(db_session, sample_signup_input):
    # Insert user and verify
    insert_stmt = insert(User).values(sample_signup_input)
    db_session.execute(insert_stmt)
    db_session.commit()
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()
    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

# Test user signup with invalid data (test case expected to fail)
def test_signup_invalid_data(db_session):
    invalid_input = {'FirstName': '', 'LastName': 'Phippen', 'Email': 'invalid_email', 'PhoneNumber': '123', 'Password': 'pass'}
    insert_stmt = insert(User).values(invalid_input)
    try:
        db_session.execute(insert_stmt)
        db_session.commit()
        assert False, "Expected an error due to invalid data"
    except Exception:
        assert True

# Test login with correct credentials
def test_login_correct_credentials(db_session, sample_signup_input):
    # Insert user
    insert_stmt = insert(User).values(sample_signup_input)
    db_session.execute(insert_stmt)
    db_session.commit()
    # Attempt login
    get_password = select(User.Password).where(User.Email == sample_signup_input['Email'])
    user_password = db_session.execute(get_password).fetchone()
    assert user_password[0] == sample_signup_input['Password']

# Test login with incorrect credentials
def test_login_incorrect_credentials(db_session):
    # Attempt login with incorrect password
    get_password = select(User.Password).where(User.Email == 'nonexistent@marist.edu')
    user_password = db_session.execute(get_password).fetchone()
    assert user_password is None

# Test critical error handling (critical error)
def test_critical_error_handling(db_session):
    # Simulate a critical error by dropping a table
    db_session.execute(text("DROP TABLE Users"))
    try:
        db_session.commit()
        assert False, "Expected a critical error due to missing table"
    except Exception:
        assert True