"""Aerial danger detection results and match types."""

from dataclasses import dataclass, field
from enum import Enum


class DangerType(str, Enum):
    """Enum of supported aerial danger types."""

    BALLISTIC = "ballistic"
    CRUISE = "cruise"
    DRONE = "drone"
    GENERIC = "generic"
    GUIDED_BOMB = "guided_bomb"
    IRBM = "irbm"
    MLRS = "mlrs"


@dataclass
class PatternMatch:
    """Represents text matched by a regex pattern."""

    text: str
    pattern: str


class DetectionStatus(str, Enum):
    """How a message affects an existing danger state."""

    DANGER = "danger"
    SAFE = "safe"
    IGNORED = "ignored"


@dataclass
class Detection:
    """Represents a detected aerial danger."""

    danger: bool
    message: str
    type: DangerType | None = None
    matched_area: str | None = None
    matched_danger: str | None = None
    area_pattern: str | None = None
    danger_pattern: str | None = None
    status: DetectionStatus = field(default=DetectionStatus.IGNORED, kw_only=True)
