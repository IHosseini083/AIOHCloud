import attrs


@attrs.define
class Location:
    """Representation of a location."""

    id: int
    name: str
    city: str
    country: str
    description: str
    latitude: float
    longitude: float
    network_zone: str
