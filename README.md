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

## Generators module
The generators.py module contains generator functions for working with transaction
data and generating card numbers. Generators allow efficient iteration without loading
all data into memory at once.

Functions
1. filter_by_currency

Filters transactions by currency code.
Parameters:
transactions — list of transaction dictionaries
currency_code — currency code to filter (e.g., "USD")

Returns:
Iterator of transactions matching the specified currency

Example:

from src.generators import filter_by_currency

transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        },
        "description": "Payment in USD"
    },
    {
        "operationAmount": {
            "currency": {"code": "RUB"}
        },
        "description": "Payment in RUB"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction["description"])

2. transaction_descriptions

Returns descriptions of all transactions.
Parameters:
transactions — list of transaction dictionaries

Returns:
Iterator of description strings

Example:

from src.generators import transaction_descriptions

transactions = [
    {"description": "Transfer to account"},
    {"description": "Card payment"}
]

descriptions = transaction_descriptions(transactions)

for desc in descriptions:
    print(desc)

3. card_number_generator

Generates card numbers in the format:
XXXX XXXX XXXX XXXX

Parameters:
start — starting number (inclusive)
stop — ending number (inclusive)

Returns:
Iterator of formatted card numbers

Example:

from src.generators import card_number_generator

generator = card_number_generator(1, 3)

for card in generator:
    print(card)

## Code Quality
1. The project uses:
- flake8 for style checking
- mypy for static type checking
2. Run checks:
```bash
poetry run flake8 .
poetry run mypy .
```
## Testing
Running tests:
poetry run pytest

Checking the coverage:
poetry run pytest --cov=src --cov-report=html

## Documentation

All functions include docstrings describing parameters and return values.

## Working with CSV and Excel

The `readers.py` module has been added, which allows you to:

- read data from CSV files (`read_csv`)
- read data from Excel files (`read_excel`)

Both functions return a list of dictionaries with transactions.
If errors occur or the file is empty, an empty list is returned.