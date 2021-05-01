from unittest import TestCase
from Package1.Worker import Worker


class TestWorker(TestCase):
    def test_full_name(self):
        bob = Worker('bob', 'Cohen', 1980, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        self.assertTrue(bob.full_name() == 'bob Cohen')
        self.assertIn('bob', bob.full_name())

    def test_age_past(self):
        bob = Worker('bob', 'Cohen', 1980, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        print(bob.age())
        self.assertIn('41', bob.age())

    def test_age_future(self):
        mati = Worker('Mati', 'Levi', 2022, 1,1,'1 Yigal Alon, Tel Aviv', 'il')
        self.assertIn('Error', mati.age())

    def test_age_current_year(self):
        mati = Worker('Mati', 'Levi', 2021, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        self.assertIn('0', mati.age())

    def test_days_to_birthday_future(self):
        mati = Worker('Mati', 'Levi', 1980, 7, 30, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('93 days', mati.days_to_birthday())

    def test_days_to_birthday_past(self):
        mati = Worker('Mati', 'Levi', 1980, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('248 days', mati.days_to_birthday())

    def test_days_to_birthday_today(self):
        mati = Worker('Mati', 'Levi', 1980, 4, 28, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('0', mati.days_to_birthday())

    # def test_days_to_birthday_30_2(self):
    #     mati = Worker('Mati', 'Levi', 1980, 2, 30, '1 Yigal Alon, Tel Aviv', 'il')
    #     print(mati.days_to_birthday())
    #     # self.assertIn('57 days', mati.days_to_birthday())
    #     self.assertRaises(msg='day is out of range for month')


    def test_greet(self):
        pass

    def test_location(self):
        pass
