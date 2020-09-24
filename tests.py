import unittest
import hello as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        self.assertEqual(
            r.data,
            b'\xd0\xa3 \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x[80 chars]x8c!'
        )

    def test_post(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()
