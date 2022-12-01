from typing import Any, Dict, Optional, Tuple, Type, TypeVar

import attrs

_T = TypeVar("_T", bound="BaseModel")


class BaseModel:
    __slots__: Tuple[str, ...] = ()

    @classmethod
    def from_dict(cls: Type[_T], data: Dict[str, Any]) -> _T:
        return cls(**{k: v for k, v in data.items() if k in cls.__slots__})


@attrs.define
class Pagination(BaseModel):
    """Pagination object in a `meta` object."""

    page: int
    per_page: int
    previous_page: Optional[int]
    next_page: Optional[int]
    last_page: int
    total_entries: int


@attrs.define
class Meta(BaseModel):
    """Model representing `meta` object of an API response."""

    pagination: Pagination
