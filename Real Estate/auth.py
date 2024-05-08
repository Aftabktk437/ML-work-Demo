# auth.py
import joblib
import streamlit as st
import sqlite3
import hashlib
from urllib.parse import urlencode

# Global variables for connection and cursor
conn = None
cursor = None


def create_connection():
    global conn, cursor
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()


def create_users_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')


def insert_user(cursor, name, email, password):
    # Check if user already exists
    if get_user_by_email(cursor, email):
        return False  # User exists
    cursor.execute('''
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    ''', (name, email, password))
    conn.commit()
    return True  # User added


def get_user_by_email(cursor, email):
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    return cursor.fetchone()


def main():
    create_connection()
    st.title("House Price Prediction")
    st.write("Please enter the details of the house to predict its price.")

    # Input fields for user signup
    st.subheader("Sign Up")
    name = st.text_input("Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input(
        "Password", type="password", key="signup_password")
    confirm_password = st.text_input(
        "Confirm Password", type="password", key="confirm_password")
    if st.button("Sign Up"):
        if password == confirm_password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            create_users_table(cursor)
            if insert_user(cursor, name, email, hashed_password):
                st.success("Sign up successful! Please sign in.")
                params = {"page": "home"}
                st.experimental_set_query_params(**params)
            else:
                st.error("User already exists. Please sign in.")
        else:
            st.error("Passwords do not match.")

    # Input fields for user signin
    st.subheader("Sign In")
    signin_email = st.text_input("Email", key="signin_email")
    signin_password = st.text_input(
        "Password", type="password", key="signin_password")
    if st.button("Sign In"):
        user = get_user_by_email(cursor, signin_email)
        if user:
            if hashlib.sha256(signin_password.encode()).hexdigest() == user[3]:
                st.success("Sign in successful!")
                params = {"page": "home"}
                st.experimental_set_query_params(**params)
            else:
                st.error("Incorrect password.")
        else:
            st.error("User does not exist.")

    # Input fields for house price prediction
    st.subheader("House Price Prediction!")


if __name__ == "__main__":
    main()


# import joblib
# import streamlit as st
# import sqlite3
# import hashlib
# from urllib.parse import urlencode

# # Global variables for connection and cursor
# conn = None
# cursor = None

# # Function to create a SQLite connection and cursor


# def create_connection():
#     global conn, cursor
#     conn = sqlite3.connect('user_database.db')
#     cursor = conn.cursor()

# # Function to create the users table if it doesn't exist


# def create_users_table(cursor):
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT,
#                         email TEXT UNIQUE,
#                         password TEXT)''')

# # Function to insert a new user into the users table


# def insert_user(cursor, name, email, password):
#     cursor.execute('''INSERT INTO users (name, email, password)
#                       VALUES (?, ?, ?)''', (name, email, password))
#     conn.commit()

# # Function to retrieve a user by email from the users table


# def get_user_by_email(cursor, email):
#     cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
#     return cursor.fetchone()

# # Streamlit UI


# def main():
#     create_connection()
#     st.title("House Price Prediction")
#     st.write("Please enter the details of the house to predict its price.")

#     # Input fields for user signup
#     st.subheader("Sign Up")
#     name = st.text_input("Name", key="signup_name")
#     email = st.text_input("Email", key="signup_email")
#     password = st.text_input(
#         "Password", type="password", key="signup_password")
#     confirm_password = st.text_input(
#         "Confirm Password", type="password", key="confirm_password")
#     if st.button("Sign Up"):
#         if password == confirm_password:
#             # Encrypt password before storing it
#             hashed_password = hashlib.sha256(password.encode()).hexdigest()
#             create_users_table(cursor)
#             insert_user(cursor, name, email, hashed_password)
#             st.success("Sign up successful! Please sign in.")
#             # Redirect to home page
#             params = {"page": "home"}
#             st.experimental_set_query_params(**params)

#         else:
#             st.error("Passwords do not match.")

#     # Input fields for user signin
#     st.subheader("Sign In")
#     signin_email = st.text_input("Email", key="signin_email")
#     signin_password = st.text_input(
#         "Password", type="password", key="signin_password")
#     if st.button("Sign In"):
#         user = get_user_by_email(cursor, signin_email)
#         if user:
#             # Check if the password matches the stored password after hashing
#             if hashlib.sha256(signin_password.encode()).hexdigest() == user[3]:
#                 st.success("Sign in successful!")
#                 # Redirect to home page
#                 params = {"page": "home"}
#                 st.experimental_set_query_params(**params)
#             else:
#                 st.error("Incorrect password.")
#         else:
#             st.error("User does not exist.")

#     # Input fields for house price prediction
#     st.subheader("House Price Prediction")


# if __name__ == "__main__":
#     main()
