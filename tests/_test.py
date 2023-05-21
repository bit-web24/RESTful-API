import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from src.routes import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(users, list)
        print("Test 'test_get_users' passed successfully. Users retrieved successfully.")

    def test_get_user(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(user, dict)
        self.assertIn('id', user)
        self.assertEqual(user['id'], 1)
        print("Test 'test_get_user' passed successfully. User retrieved successfully.")

    def test_get_user_not_found(self):
        response = self.app.get('/users/999')
        self.assertEqual(response.status_code, 404)
        error = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(error, dict)
        self.assertIn('error', error)
        print("Test 'test_get_user_not_found' passed successfully. User not found handled correctly.")

    def test_get_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        orders = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(orders, list)
        print("Test 'test_get_orders' passed successfully. Orders retrieved successfully.")

    def test_get_order(self):
        response = self.app.get('/orders/1')
        self.assertEqual(response.status_code, 200)
        order = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(order, dict)
        self.assertIn('id', order)
        self.assertEqual(order['id'], 1)
        print("Test 'test_get_order' passed successfully. Order retrieved successfully.")

    def test_get_order_not_found(self):
        response = self.app.get('/orders/999')
        self.assertEqual(response.status_code, 404)
        error = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(error, dict)
        self.assertIn('error', error)
        print("Test 'test_get_order_not_found' passed successfully. Order not found handled correctly.")

if __name__ == '__main__':
    unittest.main()
