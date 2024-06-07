import unittest
from main import calculate_phone_call_cost


class TestCalculatePhoneCallCost(unittest.TestCase):
    def test_valid_weekday(self):
        self.assertAlmostEqual(calculate_phone_call_cost(30, 'Monday'), 15.0)
        self.assertAlmostEqual(calculate_phone_call_cost(30, 'Friday'), 15.0)

    def test_valid_weekend(self):
        self.assertAlmostEqual(calculate_phone_call_cost(30, 'Saturday'), 12.0)
        self.assertAlmostEqual(calculate_phone_call_cost(30, 'Sunday'), 12.0)

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            calculate_phone_call_cost(-10, 'Monday')
        with self.assertRaises(ValueError):
            calculate_phone_call_cost(0, 'Monday')
        with self.assertRaises(ValueError):
            calculate_phone_call_cost('30', 'Monday')

    def test_invalid_weekday(self):
        with self.assertRaises(ValueError):
            calculate_phone_call_cost(30, 'Someday')
        with self.assertRaises(ValueError):
            calculate_phone_call_cost(30, 'Какой-то день')


if __name__ == '__main__':
    unittest.main()
