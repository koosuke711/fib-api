import unittest
from fastapi.testclient import TestClient
from main import app  # ここで 'main' をコードが保存されたファイル名に変更してください

class TestFibonacciEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    # 正しい入力（正の整数）を入力したとき
    def test_fibonacci_valid_input(self):
        response = self.client.get("/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 55})

    # 文字列を入力したとき
    def test_fibonacci_zero_input(self):
        response = self.client.get("/fib?n=aaa")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
                "status": 400,
                "message": "Badrequest."
        })

    # 負の値を入力したとき
    def test_fibonacci_negative_input(self):
        response = self.client.get("/fib?n=-1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
                "status": 400,
                "message": "Badrequest."
        })

    # 実数を入力したとき
    def test_fibonacci_negative_input(self):
        response = self.client.get("/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
                "status": 400,
                "message": "Badrequest."
        })


if __name__ == "__main__":
    unittest.main()
