import sys
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    NoReturn,
    Optional,
    Type,
    TypeVar,
    cast,
)

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from httpx import AsyncClient, Response

from aiohcloud.errors import APIError
from aiohcloud.utils import Representation

if TYPE_CHECKING:
    from aiohcloud.handlers.abc import Handler
    from aiohcloud.utils import ReprArgs

    HandlerT = TypeVar("HandlerT", bound=Handler)


def _catch_api_errors(response: Response) -> Response:
    if response.status_code not in (200, 201, 204):
        error = response.json()["error"]
        raise APIError(
            code=error["code"],
            message=error["message"],
            details=error["details"],
        )
    return response


class HetznerCloud(Representation):
    """Async client for Hetzner Cloud API."""

    API_BASE_URL: ClassVar[str] = "https://api.hetzner.cloud/v1"
    _HANDLERS: ClassVar[Dict[str, "Handler"]] = {}

    __slots__ = (
        "_token",
        "_session",
        "_headers",
    )

    def __init__(self, token: str) -> None:
        self._token = token
        self._session = AsyncClient(base_url=self.API_BASE_URL)
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    @property
    def token(self) -> str:
        """Hetzner Cloud API token."""
        return self._token

    def __repr_args__(self) -> "ReprArgs":
        return [
            ("token", "**********"),
        ]

    async def request(
        self,
        method: str,
        endpoint: str,
        json: Optional[Any] = None,
        **query_params,
    ) -> Response:
        """Make a request to the Hetzner Cloud API.

        Arguments:
            method (`str`): HTTP method.
            endpoint (`str`): API endpoint. e.g `/actions`
            json (`Mapping[str, Any]`, optional): JSON data to send. Defaults to `None`.

        Returns:
            `httpx.Response`: Response object.
        """
        response = await self._session.request(
            method=method,
            url=endpoint,
            headers=self._headers,
            json=json,
            params={k: v for k, v in query_params.items() if v},
        )
        return _catch_api_errors(response)

    def use(self, handler: Type["HandlerT"]) -> "HandlerT":
        try:
            instance = self._HANDLERS[handler.__name__]
        except KeyError:
            instance = handler(self)
            self._HANDLERS[handler.__name__] = instance
        return cast("HandlerT", instance)

    async def close(self) -> None:
        """Close the session."""
        await self._session.aclose()

    def __enter__(self) -> NoReturn:
        raise RuntimeError("Use 'async with ...' instead of 'with ...'")

    async def __aenter__(self) -> Self:  # type: ignore
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()
