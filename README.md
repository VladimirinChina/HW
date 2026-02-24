# Banking Operations Processing

## Description

This project provides utility functions for processing banking operations data.

It includes functionality for:
- Filtering operations by state
- Sorting operations by date
- Masking sensitive information

The project is structured in a modular way and includes static code analysis.


## Instalation

1. Clone the repository:
```bash
git clone https://github.com/VladimirinChina/HW.git
```
2. Install dependencies using Poetry:
```
poetry install
```
## Usage Example
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-02T10:00:00"},
]

filtered_operations = filter_by_state(operations)
sorted_operations = sort_by_date(operations)

## Code Quality
1. The project uses:
- flake8 for style checking
- mypy for static type checking
2. Run checks:
```bash
poetry run flake8 .
poetry run mypy .
```
## Documentation

All functions include docstrings describing parameters and return values.
