from abc import ABC
from typing import TYPE_CHECKING

from aiohcloud.client import HetznerCloud
from aiohcloud.utils import Representation

if TYPE_CHECKING:
    from aiohcloud.utils import ReprArgs


class Handler(Representation, ABC):
    __slots__ = ("_client",)

    def __init__(self, client: HetznerCloud) -> None:
        if not isinstance(client, HetznerCloud):
            raise TypeError(
                f"Expected client to be an instance of 'HetznerCloud', got {client!r}",
            )
        self._client = client

    def __repr_args__(self) -> "ReprArgs":
        return [
            ("client", self._client),
        ]
