import re
import sys
from typing import Any, Dict, List, Optional, Tuple

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

# Borrowed these RegEx patterns from hcloud-python project:
# https://github.com/hetznercloud/hcloud-python/blob/main/hcloud/helpers/labels.py
LABELS_KEY_RE = re.compile(
    r"^([a-z0-9A-Z]((?:[\-_.]|[a-z0-9A-Z]){0,253}[a-z0-9A-Z])?/)"
    r"?[a-z0-9A-Z]((?:[\-_.]|[a-z0-9A-Z]|){0,62}[a-z0-9A-Z])?$",
)
LABELS_VALUE_RE = re.compile(
    r"^(([a-z0-9A-Z](?:[\-_.]|[a-z0-9A-Z]){0,62})?[a-z0-9A-Z]$|$)",
)

# Type aliases
ReprArgs: TypeAlias = List[Tuple[str, Any]]


class Representation:
    """Mixin to provide __repr__ method."""

    __slots__: Tuple[str, ...] = ()

    def __repr_name__(self) -> str:
        """Return the name of the class."""
        return self.__class__.__name__

    def __repr_args__(self) -> ReprArgs:
        """Return a list of 2 length tuples containing name and value of attributes."""
        attrs = ((name, getattr(self, name)) for name in self.__slots__)
        return [(name, value) for name, value in attrs if value is not None]

    def __gen_str__(self, joiner: str) -> str:
        """Generate a string representation from the attributes."""
        attrs = self.__repr_args__()
        return joiner.join(repr(v) if not a else f"{a}={v!r}" for a, v in attrs)

    def __repr__(self) -> str:
        return f"{self.__repr_name__()}({self.__gen_str__(', ')})"


def validate_labels(labels: Dict[str, str]) -> Tuple[bool, Optional[str]]:
    """
    Validate the given labels based on rules defined by Hetzner Cloud API docs.
    Returns a tuple containing a boolean indicating if the labels are valid and
    a string representing the key/value that failed validation or `None` if everything
    is valid.
    """
    for key, value in labels.items():
        if not LABELS_KEY_RE.match(key):
            return False, key
        if not LABELS_VALUE_RE.match(value):
            return False, value
    return True, None
