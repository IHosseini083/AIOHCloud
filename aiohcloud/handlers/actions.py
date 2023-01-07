from typing import Any, Dict, Optional

from aiohcloud.enums import ActionStatus, SortOrder
from aiohcloud.handlers.abc import Handler
from aiohcloud.types import Action, ActionError, ActionResource, Paginated


def _action_from_dict(data: Dict[str, Any]) -> Action:
    data["error"] = ActionError(**e) if (e := data.get("error")) else None
    data["resources"] = [ActionResource(**r) for r in data.get("resources", [])]
    data["status"] = ActionStatus(data["status"])
    return Action(**data)


class Actions(Handler):
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
            A :class:`aiohcloud.types.Paginated` object containing which is a lazy
            iterator of :class:`aiohcloud.types.Action` objects.
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
        return Paginated[Action].from_dict(
            response,
            _action_from_dict,
            "actions",
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
        return _action_from_dict(response.json()["action"])
