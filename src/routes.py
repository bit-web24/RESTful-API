from flask import Flask
from schema import schema_init
import sqlite3
import json
import os

app = Flask(__name__)

schema_init()

# Get the project directory absolute path
root_dir = os.path.abspath(os.path.dirname(__file__))
db_path = root_dir + '/../db/database.db'

# Implement the /users endpoint to return a list of all users:
@app.route('/users', methods=['GET'])
def get_users():
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    
    users_list = []

    for user in users:
        user_dict = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'created_at': user[3]
                }
        users_list.append(user_dict)

    users_json = json.dumps(users_list)
    return users_json

# Implement the /users/{id} endpoint to return the details of a specific user:
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
    user = cursor.fetchone()

    if user:
        user_dict = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'created_at': user[3]
                }
        
        user_json = json.dumps(user_dict)
        return user_json
    else:
        msg = {
                "error": "User not found"
                }
        err = json.dumps(msg)
        return err

# Implement the /orders endpoint to return a list of all orders:
@app.route('/orders', methods=['GET'])
def get_orders():
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM orders''')
    orders = cursor.fetchall()

    orders_list = []

    for order in orders:
        order_dict = {
                'id': order[0],
                'user_id': order[1],
                'product_name': order[2],
                'quantity': order[3],
                'total_price': order[4],
                'created_at': order[5]
                }
        
        orders_list.append(order_dict)
    
    orders_json = json.dumps(orders_list)
    return orders_json

# Implement the /orders/{id} endpoint to return the details of a specific order:
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
   connect = sqlite3.connect(db_path)
   cursor = connect.cursor()
   cursor.execute('''SELECT * FROM orders WHERE id = ?''', (order_id,))
   order = cursor.fetchone()

   if order:
       order_dict = {
               'id': order[0],
               'user_id': order[1],
               'product_name': order[2],
               'quantity': order[3],
               'total_price': order[4],
               'created_at': order[5]
               }

       order_json = json.dumps(order_dict)
       return order_json
   else:
       msg = {
               "error": "Order not found"
               }
       err = json.dumps(msg)
       return err

