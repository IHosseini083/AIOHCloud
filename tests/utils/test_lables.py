from typing import Dict, Optional

import pytest

from aiohcloud.utils import validate_labels


@pytest.mark.parametrize(
    "labels, expected, target",
    [
        # Valid labels
        ({"label1": "correct.de"}, True, None),
        ({"field": ""}, True, None),
        ({"domain.com/name": "value"}, True, None),
        ({"label3-test.com/hallo": "233344444443"}, True, None),
        # Invalid labels
        ({"valid_key": "incorrect .com"}, False, "incorrect .com"),
        (
            {f"domain.com/test-{'1' * 250}": "value"},
            False,
            f"domain.com/test-{'1' * 250}",
        ),
        ({"incorrect.com/tes t": "correct.com"}, False, "incorrect.com/tes t"),
        ({"incorrect.com/+": "correct.com"}, False, "incorrect.com/+"),
    ],
)
def test_validate_labels(
    labels: Dict[str, str],
    expected: bool,
    target: Optional[str],
) -> None:
    assert validate_labels(labels) == (expected, target)
