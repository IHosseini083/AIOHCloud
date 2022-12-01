from typing import Any, Dict


class APIError(Exception):
    """
    Generic exception class for API errors specified in Hetzner Cloud Documentation.
    https://docs.hetzner.cloud/#errors
    """

    def __init__(self, code: str, message: str, details: Dict[str, Any]) -> None:
        self.code = code
        self.message = message
        self.details = details

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"
