from app import negative_sum, app
import unittest

class TestNegativeSum(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_negative_sum(self):
        result = self.app.post('/negative-sum/-1/-1')
        print("result: ",result.get_json())
        self.assertEqual(result.get_json()['sum'], -2)

if __name__ == "__main__":
    unittest.main()