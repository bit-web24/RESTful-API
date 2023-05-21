# 🚀 API Usage

This is a RESTful API that allows you to interact with the application and perform various actions. The API provides endpoints to retrieve **user data** and **order data**.

# Prerequisites

Before proceeding, ensure that you have the following installed on your system:

* Python (version >=3.11.2)
* SQLite (version 3)

# Installation

>  `NOTE`: If you are on `windows` you should skip this step

To install the `sqlite3` module for Python, you typically don't need to install it separately because it comes bundled with the standard library of Python. However, you may need to install the appropriate `SQLite database engine and development files` for your **operating system**. Here are the general steps to install SQLite:

### Linux (Ubuntu/Debian) 🐧:
1. Open a Terminal.
2. Install SQLite by running the following command:

```bash
sudo apt install sqlite3 libsqlite3-dev python3.11-venv
```

# Project Setup

This guide provides step-by-step instructions to set up and run the project.

## Clone the repository to your local machine:
```bash
git clone https://github.com/bit-web24/RESTful-API.git
```

## Navigate to the project directory:
```bash
cd RESTful-API
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the virtual environment:

### For Windows:
```bash
venv\Scripts\activate
```

### For macOS/Linux:
```bash
source venv/bin/activate
```

## Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

## Base URL

The base URL for all API endpoints is: http://127.0.0.1:5000

## Authentication

Authentication is not required to access the API endpoints.

## Endpoints

### Get Users
Retrieve a list of all users.

* **Endpoint**: `/users`
* **Method**: `GET`
* **Response**: List of users in JSON format

### Get User
Retrieve a specific user by their ID.

* **Endpoint**: `/users/{id}`
* **Method**: `GET`
* **Parameters**:
    `{id}`: ID of the user to retrieve
* **Response**: User object in JSON format

### Get Orders
Retrieve a list of all orders.

* **Endpoint**: `/orders`
* **Method**: `GET`
* **Response**: List of orders in JSON format

### Get Order
Retrieve a specific order by its ID.

* **Endpoint**: `/orders/{id}`
* **Method**: `GET`
* **Parameters**:
	`{id}`: ID of the order to retrieve
* **Response**: Order object in JSON format

## Error Handling

If an error occurs while processing a request, the API will return an error response in the following format:

```json
{
  "error": "Error message"
}
```

The error field will contain a descriptive error message indicating the nature of the error.

## Status Codes

The API may return the following status codes in the responses:

* `200 OK`: The request was successful.
* `404 Not Found`: The requested resource was not found.
* `500 Internal Server Error`: An error occurred on the server.

# Running Tests

To run the tests, use the following command:

```bash
pytest
```

`NOTE: Run in the RESTful-API director`

# Examples

## Retrieve all users

**Request**:
```bash
GET /users
```


Response:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2023-05-20 10:00:00"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "created_at": "2023-05-20 11:00:00"
  }
]
```

## Retrieve a user

**Request**:

```bash
GET /users/1
```

**Response**:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2023-05-20 10:00:00"
}
```

## Retrieve all orders

**Request**:

```bash
GET /orders
```

**Response**:
```json
[
  {
    "id": 1,
    "user_id": 1,
    "product_name": "Product A",
    "quantity": 2,
    "total_price": 20.0,
    "created_at": "2023-05-20 10:30:00"
  },
  {
    "id": 2,
    "user_id": 2,
    "product_name": "Product B",
    "quantity": 1,
    "total_price": 15.0,
    "created_at": "2023-05-20 11:30:00"
  }
]
```

## Retrieve an order

**Request**:

```bash
GET /orders/2
```

**Response**:

```json
{
  "id": 2,
  "user_id": 2,
  "product_name": "Product B",
  "quantity": 1,
  "total_price": 15.0,
  "created_at": "2023-05-20 11:30:00"
}
```

# Conclusion

This README provides an overview of the available API endpoints and their usage. Feel free to explore and interact with the API to perform the desired actions. If you have any questions or issues, please contact me at `bitweb24@gmail.com`.

Happy API integration!
