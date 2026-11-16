import unittest

from unit_converter import (
    celsius_to_fahrenheit,
    convert,
    convert_length,
    convert_many,
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


class ParseTests(unittest.TestCase):
    def test_parse_conversion_expression(self):
        from unit_converter import parse_conversion

        self.assertEqual(parse_conversion("5 km -> m"), (5.0, "km", "m"))
        self.assertEqual(parse_conversion("  12.5 KG to lb "), (12.5, "kg", "lb"))

    def test_parse_rejects_garbage(self):
        from unit_converter import parse_conversion

        with self.assertRaises(ValueError):
            parse_conversion("five km to m")


class ConvertManyTests(unittest.TestCase):
    def test_converts_multiple_lines(self):
        results = convert_many("5 km -> m\n100 cm to m")
        self.assertEqual(len(results), 2)
        self.assertEqual(
            results[0],
            {
                "input": "5 km -> m",
                "value": 5.0,
                "from": "km",
                "to": "m",
                "result": 5000.0,
            },
        )
        self.assertEqual(results[1]["result"], 1.0)

    def test_blank_lines_are_skipped(self):
        results = convert_many("5 km -> m\n\n   \n1 kg to lb\n")
        self.assertEqual([item["input"] for item in results], ["5 km -> m", "1 kg to lb"])

    def test_invalid_line_raises(self):
        with self.assertRaises(ValueError):
            convert_many("5 km -> m\nnot a conversion")


if __name__ == "__main__":
    unittest.main()
