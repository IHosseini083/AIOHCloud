from typing import TYPE_CHECKING, ClassVar, Dict, Type, TypeVar, cast

from httpx import AsyncClient, Response

from aiohcloud.errors import APIError
from aiohcloud.utils import Representation

if TYPE_CHECKING:
    from aiohcloud.handlers import Handler

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
    """Base async client for Hetzner Cloud API."""

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

    async def request(self, method: str, endpoint: str, **query_params) -> Response:
        """Make a request to the Hetzner Cloud API.

        Arguments:
            method (`str`): HTTP method.
            endpoint (`str`): API endpoint. e.g `/actions`

        Returns:
            `httpx.Response`: Response object.
        """
        response = await self._session.request(
            method=method,
            url=endpoint,
            headers=self._headers,
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

    def __enter__(self) -> "HetznerCloud":
        raise RuntimeError("Use async with instead.")

    async def __aenter__(self) -> "HetznerCloud":
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()
