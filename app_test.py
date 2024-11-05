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
        self.assertEqual(result.get_json()['sum'], -2)

    def test_negative_find(self):
        result = self.app.get('/filter-by-results/aerger')
        self.assertNotEqual(result.status_code,200)

if __name__ == "__main__":
    unittest.main()