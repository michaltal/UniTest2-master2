from unittest import TestCase
from unittest.mock import patch
from Package1.Worker import Worker
import datetime
import requests

class TestWorker(TestCase):
    def setUp(self):
        print('setUp')
        self.moshe = Worker('Moshe', 'Cohen', 2000, 2, 17, '1 Yigal Alon, Tel Aviv', 'il')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        res = self.moshe.full_name()
        self.assertTrue(res == 'Moshe Cohen')


    def test_location(self):
        with patch('Package1.Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            res = self.moshe.location()
            self.assertEqual(res, 'Success')

