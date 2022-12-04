from typing import List, Optional

import attrs

from aiohcloud.enums.actions import ActionStatus


@attrs.define
class ActionResource:
    """Model representing a resource that an action relates to."""

    id: int
    type: str


@attrs.define
class ActionError:
    """Represents an error that occurred during an action."""

    code: str
    message: str


@attrs.define
class Action:
    """Represents an `action` object."""

    id: int
    command: str
    error: Optional[ActionError]
    started: str
    finished: Optional[str]  # Can be None if action is still running
    progress: int
    resources: Optional[List[ActionResource]]
    status: ActionStatus
