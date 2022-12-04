from typing import Generic, Iterator, List, Optional, TypeVar

import attrs

_T = TypeVar("_T")


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
    """Model representing a paginated API response."""

    results: List[_T]
    meta: Meta

    def __iter__(self) -> Iterator[_T]:
        return iter(self.results)
