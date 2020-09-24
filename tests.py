import unittest
import hello as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        res = 'У меня получилось!'
        self.assertEqual(r.data, res.encode('utf-8'))

    def test_post(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()
