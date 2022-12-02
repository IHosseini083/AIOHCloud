from enum import Enum


class ActionStatus(str, Enum):
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
