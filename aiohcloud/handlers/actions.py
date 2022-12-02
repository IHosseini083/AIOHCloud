from typing import TYPE_CHECKING, Any, Dict, Optional

from aiohcloud.enums import ActionStatus, SortOrder
from aiohcloud.models import (
    Action,
    ActionError,
    ActionResource,
    Meta,
    Paginated,
    Pagination,
)
from aiohcloud.utils import Representation

if TYPE_CHECKING:
    from aiohcloud.client import HetznerCloud


def action_from_dict(data: Dict[str, Any]) -> Action:
    data["error"] = ActionError(**e) if (e := data.get("error")) else None
    data["resources"] = [ActionResource(**r) for r in data.get("resources", [])]
    data["status"] = ActionStatus(data["status"])
    return Action(**data)


class Actions(Representation):
    __slots__ = ("_client",)

    def __init__(self, client: "HetznerCloud") -> None:
        self._client = client

    async def get_actions(
        self,
        sort: Optional[str] = None,
        sort_order: Optional[SortOrder] = None,
        status: Optional[str] = None,
        page: int = 1,
        per_page: int = 50,
    ) -> Paginated[Action]:
        """Get all actions.

        Arguments:
            sort (`str`, optional): Name of the attribute to sort by. Defaults to None.
            sort_order (`SortOrder`, optional): Sort order. Defaults to None.
            status (`str`, optional): Filter by status. Defaults to None.
            page (`int`, optional): Page number. Defaults to 1.
            per_page (`int`, optional): Number of actions per page. Defaults to 50.

        Returns:
            `Paginated[Action]`: Paginated object containing a list of actions and
            pagination metadata (e.g. total number of actions).
        """
        if status is not None and status.upper() not in ActionStatus.__members__:
            raise ValueError(f"Invalid status: {status!r}") from None
        if sort is not None:
            if sort_order is not None:
                sort = f"{sort}:{sort_order.value}"
        response = (
            await self._client.request(
                method="GET",
                endpoint="/actions",
                page=page,
                per_page=per_page,
                status=status,
                sort=sort,
            )
        ).json()
        return Paginated(
            results=[action_from_dict(a) for a in response["actions"]],
            meta=Meta(
                pagination=Pagination(**response["meta"]["pagination"]),
            ),
        )

    async def get_action(self, action_id: int) -> Action:
        """Get an action by ID.

        Arguments:
            action_id (`int`): Action ID.

        Returns:
            `Action`: Action object.
        """
        response = await self._client.request(
            method="GET",
            endpoint=f"/actions/{action_id}",
        )
        return action_from_dict(response.json()["action"])
