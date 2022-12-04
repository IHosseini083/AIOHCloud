from typing import TYPE_CHECKING, Any, AsyncGenerator, Dict, Optional, Tuple

from aiohcloud.types.datacenters import Datacenter, DatacenterServerTypes
from aiohcloud.types.locations import Location
from aiohcloud.utils import Representation

if TYPE_CHECKING:
    from aiohcloud.client import HetznerCloud


def _datacenter_from_dict(datacenter: Dict[str, Any]) -> Datacenter:
    datacenter["location"] = Location(**datacenter["location"])
    datacenter["server_types"] = DatacenterServerTypes(
        **datacenter["server_types"],
    )
    return Datacenter(**datacenter)


class Datacenters(Representation):
    __slots__ = ("_client",)

    def __init__(self, client: "HetznerCloud") -> None:
        self._client = client

    async def get_datacenters(
        self,
        name: Optional[str] = None,
    ) -> AsyncGenerator[Tuple[Datacenter, int], None]:
        """Get all datacenters.

        Arguments:
            name (`str`, optional): Filter datacenters by name. Defaults to `None`.
            The response will only contain the datacenter matching the specified name.

        Yields:
            A tuple of (datacenter, recommendation) where 'datacenter' is a
            :class:`~aiohcloud.types.Datacenter` object and 'recommendation' is an
            integer representing the id of the datacenter which is recommended to
            be used to create new servers.

        Raises:
            :class:`~aiohcloud.errors.APIError` error with code `invalid_input` if
            the given name does not match the datacenter name format.
        """
        response = await self._client.request(
            method="GET",
            endpoint="/datacenters",
            name=name,
        )
        content = response.json()
        for datacenter in content["datacenters"]:
            yield _datacenter_from_dict(datacenter), content["recommendation"]

    async def get_datacenter(self, datacenter_id: int) -> Datacenter:
        """Get a datacenter by its id.

        Arguments:
            datacenter_id (`int`): Datacenter ID.

        Returns:
            A :class:`~aiohcloud.types.Datacenter` object.

        """
        response = await self._client.request(
            method="GET",
            endpoint=f"/datacenters/{datacenter_id}",
        )
        return _datacenter_from_dict(response.json()["datacenter"])
