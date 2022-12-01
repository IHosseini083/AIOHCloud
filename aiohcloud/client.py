from typing import ClassVar

from httpx import AsyncClient, Response

from aiohcloud.errors import APIError


def _catch_api_errors(response: Response) -> Response:
    if response.status_code not in (200, 201, 204):
        error = response.json()["error"]
        raise APIError(
            code=error["code"],
            message=error["message"],
            details=error["details"],
        )
    return response


class HetznerCloud:
    """Base async client for Hetzner Cloud API.

    Arguments:
        token (`str`): Hetzner Cloud API token.
    """

    API_BASE_URL: ClassVar[str] = "https://api.hetzner.cloud/v1"

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
            params=query_params,
        )
        return _catch_api_errors(response)
