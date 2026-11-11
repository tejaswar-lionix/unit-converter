import unittest

from unit_converter import (
    celsius_to_fahrenheit,
    convert,
    convert_length,
    convert_weight,
    fahrenheit_to_celsius,
)


class UnitTests(unittest.TestCase):
    def test_length_conversion(self):
        self.assertEqual(convert_length(1, "km", "m"), 1000.0)
        self.assertEqual(convert_length(100, "cm", "m"), 1.0)

    def test_weight_conversion(self):
        self.assertAlmostEqual(convert_weight(1, "kg", "lb"), 2.204622, places=5)
        self.assertEqual(convert_weight(1000, "g", "kg"), 1.0)

    def test_temperature_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)

    def test_dispatch(self):
        self.assertEqual(convert(5, "KM", "M"), 5000.0)
        self.assertEqual(convert(0, "c", "f"), 32.0)

    def test_unknown_units_raise(self):
        with self.assertRaises(ValueError):
            convert(1, "m", "kg")

    def test_unknown_single_unit_raises(self):
        with self.assertRaises(ValueError):
            convert_length(1, "mile", "m")


if __name__ == "__main__":
    unittest.main()
