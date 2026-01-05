from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Action(Enum):
    ACCEPT = "accept"
    REVISE = "revise"
    REJECT = "reject"


@dataclass
class Decision:
    action: Action
    target: Optional[str]
    rationale: str
