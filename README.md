# unit-converter

Convert length, weight, and temperature values.

## Usage

```bash
python3 -c "from unit_converter import convert; print(convert(5, 'km', 'm'))"
python3 -c "from unit_converter import convert_many; print(convert_many('5 km -> m\n1 kg to lb'))"
```

## Features

- Length and weight conversion with validation
- Celsius and Fahrenheit conversion
- Expression parsing with parse_conversion('5 km -> m')
- Batch conversion with convert_many('5 km -> m\n1 kg to lb')

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
