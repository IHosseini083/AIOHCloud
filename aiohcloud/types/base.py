from typing import Any, Callable, Dict, Generic, Iterator, List, Optional, TypeVar

import attrs

_T = TypeVar("_T")

DictStrAny = Dict[str, Any]


@attrs.define
class Pagination:
    """Pagination object in a `meta` object."""

    page: int
    per_page: int
    previous_page: Optional[int]
    next_page: Optional[int]
    last_page: int
    total_entries: int


@attrs.define
class Meta:
    """Model representing `meta` object of an API response."""

    pagination: Pagination


@attrs.define
class Paginated(Generic[_T]):
    """
    A lazy iterator object that represents a paginated API response.
    """

    meta: Meta
    _converter: Callable[[DictStrAny], _T] = attrs.field(repr=False)
    _data: List[DictStrAny] = attrs.field(repr=False)
    _items_key: str = attrs.field(repr=False)

    @classmethod
    def from_dict(
        cls,
        data: DictStrAny,
        converter: Callable[[DictStrAny], _T],
        items_key: str,
    ) -> "Paginated[_T]":
        """Create a Paginated object from a dictionary."""
        return cls(
            meta=Meta(
                pagination=Pagination(**data["meta"]["pagination"]),
            ),
            converter=converter,
            data=data[items_key],
            items_key=items_key,
        )

    def __iter__(self) -> Iterator[_T]:
        return (self._converter(item) for item in self._data)

    def __len__(self) -> int:
        return len(self._data)
