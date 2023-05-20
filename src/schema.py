import sqlite3
from seed import users_data, orders_data
import os

def schema_init():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    connect = sqlite3.connect(root_dir + '/../db/database.db')
    print('connection to database [OK]')

    # Create a cursor object to execute SQL statements
    cursor = connect.cursor()

    # Drop the 'users' and 'orders' tables if they exist
    cursor.execute('''DROP TABLE IF EXISTS users''')
    cursor.execute('''DROP TABLE IF EXISTS orders''')
    
    # Create the 'users' table
    connect.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        created_at TIMESTAMP
    )''')
    
    print("creating users table [OK]")
    
    # Create the 'orders' table
    connect.execute('''CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        quantity INTEGER,
        total_price REAL,
        created_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')
    
    print("creating orders table [OK]")
    
    # Execute insert command for all users_data
    cursor.executemany('''INSERT INTO users (id, name, email, created_at) VALUES (?, ?, ?, ?)''', users_data)
    
    # Execute insert command for all orders_data
    cursor.executemany('''INSERT INTO orders (id, user_id, product_name, quantity, total_price, created_at) VALUES (?, ?, ?, ?, ?, ?)''', orders_data)
    
    # Commit the changes and close the connection
    connect.commit()
    connect.close()
