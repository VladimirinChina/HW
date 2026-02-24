from typing import Dict, List

import pytest


@pytest.fixture
def operations() -> List[Dict[str, str | int]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2023-02-01"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-01"},
    ]
