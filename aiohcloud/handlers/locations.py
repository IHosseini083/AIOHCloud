from typing import AsyncGenerator, Optional

from aiohcloud.handlers.abc import Handler
from aiohcloud.types.locations import Location


class Locations(Handler):
    async def get_locations(
        self,
        name: Optional[str] = None,
    ) -> AsyncGenerator[Location, None]:
        """
        Get all locations.

        Arguments:
            name (`str`, optional): Filter locations by name. Defaults to `None`.

        Yields:
            A :class:`aiohcloud.types.Location` object.
        """
        response = await self._client.request(
            method="GET",
            endpoint="/locations",
            name=name,
        )
        content = response.json()
        for location in content["locations"]:
            yield Location(**location)

    async def get_location(self, location_id: int) -> Location:
        """Get a location by its id."""
        response = await self._client.request(
            method="GET",
            endpoint=f"/locations/{location_id}",
        )
        return Location(**response.json()["location"])
