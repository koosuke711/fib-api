import unittest
from fastapi.testclient import TestClient
from fastapi_fibonacci.main import app  # パスを修正

class TestFibonacciEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    # 正しい入力（正の整数）を入力したとき
    def test_fibonacci_valid_input(self):
        response = self.client.get("/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 55})

    # 文字列を入力したとき
    def test_fibonacci_string_input(self):
        response = self.client.get("/fib?n=aaa")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "status": 400,
            "message": "入力が無効です。整数を入力してください。"
        })

    # 負の値を入力したとき
    def test_fibonacci_negative_input(self):
        response = self.client.get("/fib?n=-1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "status": 400,
            "message": "負の整数が入力されています。正の整数を入力してください。"
        })

    # 実数を入力したとき
    def test_fibonacci_float_input(self):
        response = self.client.get("/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "status": 400,
            "message": "入力が無効です。整数を入力してください。"
        })


if __name__ == "__main__":
    unittest.main()
