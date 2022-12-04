from typing import List

import attrs

from aiohcloud.types.locations import Location


@attrs.define
class DatacenterServerTypes:
    """Represents the type servers a datacenter han handle."""

    available: List[int]
    available_for_migration: List[int]
    supported: List[int]


@attrs.define
class Datacenter:
    """Representation of a datacenter."""

    id: int
    name: str
    description: str
    location: Location
    server_types: DatacenterServerTypes
