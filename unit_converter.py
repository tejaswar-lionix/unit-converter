#!/usr/bin/env python3
"""Convert length, weight, and temperature values."""
LENGTH_FACTORS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
}
WEIGHT_FACTORS = {
    "g": 0.001,
    "kg": 1.0,
    "lb": 0.45359237,
    "oz": 0.028349523125,
}
VOLUME_FACTORS = {
    "ml": 0.001,
    "l": 1.0,
    "cup": 0.2365882365,
    "gal": 3.785411784,
    "floz": 0.0295735295625,
}
SPEED_FACTORS = {
    "ms": 1.0,
    "kmh": 0.2777777778,
    "mph": 0.44704,
    "kn": 0.5144444444,
}


def convert_length(value, from_unit, to_unit):
    if from_unit not in LENGTH_FACTORS:
        raise ValueError(f"unknown length unit: {from_unit}")
    if to_unit not in LENGTH_FACTORS:
        raise ValueError(f"unknown length unit: {to_unit}")
    return round(value * LENGTH_FACTORS[from_unit] / LENGTH_FACTORS[to_unit], 6)


def convert_weight(value, from_unit, to_unit):
    if from_unit not in WEIGHT_FACTORS:
        raise ValueError(f"unknown weight unit: {from_unit}")
    if to_unit not in WEIGHT_FACTORS:
        raise ValueError(f"unknown weight unit: {to_unit}")
    return round(value * WEIGHT_FACTORS[from_unit] / WEIGHT_FACTORS[to_unit], 6)


def convert_volume(value, from_unit, to_unit):
    if from_unit not in VOLUME_FACTORS:
        raise ValueError(f"unknown volume unit: {from_unit}")
    if to_unit not in VOLUME_FACTORS:
        raise ValueError(f"unknown volume unit: {to_unit}")
    return round(value * VOLUME_FACTORS[from_unit] / VOLUME_FACTORS[to_unit], 6)


def convert_speed(value, from_unit, to_unit):
    if from_unit not in SPEED_FACTORS:
        raise ValueError(f"unknown speed unit: {from_unit}")
    if to_unit not in SPEED_FACTORS:
        raise ValueError(f"unknown speed unit: {to_unit}")
    return round(value * SPEED_FACTORS[from_unit] / SPEED_FACTORS[to_unit], 6)


def celsius_to_fahrenheit(value):
    return round(value * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(value):
    return round((value - 32) * 5 / 9, 2)


def convert(value, from_unit, to_unit):
    source = from_unit.lower()
    target = to_unit.lower()
    if source in LENGTH_FACTORS and target in LENGTH_FACTORS:
        return convert_length(value, source, target)
    if source in WEIGHT_FACTORS and target in WEIGHT_FACTORS:
        return convert_weight(value, source, target)
    if source in VOLUME_FACTORS and target in VOLUME_FACTORS:
        return convert_volume(value, source, target)
    if source in SPEED_FACTORS and target in SPEED_FACTORS:
        return convert_speed(value, source, target)
    if {source, target} <= {"c", "f"}:
        if source == target:
            return round(float(value), 2)
        if source == "c":
            return celsius_to_fahrenheit(value)
        return fahrenheit_to_celsius(value)
    raise ValueError(f"unsupported conversion: {from_unit} to {to_unit}")


def format_conversion(value, from_unit, to_unit):
    result = convert(value, from_unit, to_unit)
    return f"{value} {from_unit} = {result} {to_unit}"


def parse_conversion(text):
    """Parse text like '5 km -> m' into (5.0, 'km', 'm')."""
    import re

    match = re.fullmatch(
        r"\s*(-?\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*(?:->|to)\s*([a-zA-Z]+)\s*",
        text,
    )
    if not match:
        raise ValueError("expected format: 5 km -> m")
    value, source, target = match.groups()
    return float(value), source.lower(), target.lower()


def convert_many(text):
    """Convert newline-separated expressions into a list of result dictionaries."""
    results = []
    for line in text.splitlines():
        if not line.strip():
            continue
        value, source, target = parse_conversion(line)
        results.append(
            {
                "input": line,
                "value": value,
                "from": source,
                "to": target,
                "result": convert(value, source, target),
            }
        )
    return results


def list_units():
    """Return the supported units grouped by measurement category."""
    return {
        "length": sorted(LENGTH_FACTORS),
        "weight": sorted(WEIGHT_FACTORS),
        "volume": sorted(VOLUME_FACTORS),
        "speed": sorted(SPEED_FACTORS),
        "temperature": ["c", "f"],
    }
