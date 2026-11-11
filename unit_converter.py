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
    if {source, target} <= {"c", "f"}:
        if source == target:
            return round(float(value), 2)
        if source == "c":
            return celsius_to_fahrenheit(value)
        return fahrenheit_to_celsius(value)
    raise ValueError(f"unsupported conversion: {from_unit} to {to_unit}")
