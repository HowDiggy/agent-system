from enum import Enum
from dataclasses import dataclass


class Severity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class Dimension(Enum):
    CORRECTNESS = "correctness"
    RELIABILITY = "reliability"
    OPERABILITY = "operability"
    SECURITY = "security"
    COMPLEXITY = "complexity"

@dataclass(frozen=True)
class Critique:
    issue: str
    severity: Severity
    dimension: Dimension
    resolvable: bool
    rationale: str

