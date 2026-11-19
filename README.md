# unit-converter

Convert length, weight, volume, speed, and temperature values.

## Usage

```bash
python3 -c "from unit_converter import convert; print(convert(5, 'km', 'm'))"
python3 -c "from unit_converter import convert; print(convert(1, 'gal', 'l'))"
python3 -c "from unit_converter import convert; print(convert(1, 'mph', 'kmh'))"
python3 -c "from unit_converter import format_conversion; print(format_conversion(5, 'km', 'm'))"
python3 -c "from unit_converter import convert_many; print(convert_many('5 km -> m\n1 kg to lb'))"
```

## Features

- Length, weight, and volume conversion with validation
- Speed conversion across m/s, km/h, mph, and knots
- Celsius and Fahrenheit conversion
- Formatted output with format_conversion(5, 'km', 'm')
- Expression parsing with parse_conversion('5 km -> m')
- Batch conversion with convert_many('5 km -> m\n1 kg to lb')

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
