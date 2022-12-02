from typing import TYPE_CHECKING, Protocol, runtime_checkable

from .actions import Actions

if TYPE_CHECKING:
    from aiohcloud.client import HetznerCloud


@runtime_checkable
class Handler(Protocol):
    _client: "HetznerCloud"

    def __init__(self, client: "HetznerCloud") -> None:
        ...
