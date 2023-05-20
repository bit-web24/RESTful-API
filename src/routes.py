from flask import Flask
from flask import jsonify
from schema import connect

app = Flask(__name__)

# Implement the /users endpoint to return a list of all users:
@app.route('/users', methods=['GET'])
def get_users():
    # Retrieve all users from the database
    users = connect.execute("")
    # Convert the data to a JSON format
    # Return the JSON response
    return "list of all users"

# Implement the /users/{id} endpoint to return the details of a specific user:
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Retrieve the user with the given ID from the database
    # Convert the user data to a JSON format
    # Return the JSON response
    return "details of a user"

# Implement the /orders endpoint to return a list of all orders:
@app.route('/orders', methods=['GET'])
def get_orders():
    # Retrieve all orders from the database
    # Convert the data to a JSON format
    # Return the JSON response
    return "list of all oreders"

# Implement the /orders/{id} endpoint to return the details of a specific order:
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Retrieve the order with the given ID from the database
    # Convert the order data to a JSON format
    # Return the JSON response
    return "details of a specific order"

