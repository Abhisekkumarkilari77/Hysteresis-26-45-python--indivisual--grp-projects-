# models.py
import time
import uuid
from dataclasses import dataclass, field
from typing import Optional, Tuple

@dataclass
class User:
    user_id: str
    role: str  # driver / passenger

@dataclass
class DriverState:
    user_id: str
    lat: float
    lon: float
    available: bool = True

@dataclass
class Ride:
    ride_id: str
    passenger_id: str
    driver_id: str
    pickup: Tuple[float, float]
    dropoff: Tuple[float, float]
    status: str = "requested"
    requested_at: float = field(default_factory=time.time)
    started_at: Optional[float] = None
    ended_at: Optional[float] = None
    fare: Optional[float] = None


def new_ride_id() -> str:
    return str(uuid.uuid4())[:8]
