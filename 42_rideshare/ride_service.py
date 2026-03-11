# ride_service.py
from typing import Dict, Optional, Tuple
from .models import DriverState, Ride, User, new_ride_id
from .geoutil import haversine
from .notify import Notifier

class RideService:
    def __init__(self, notifier: Notifier):
        self.users: Dict[str, User] = {}
        self.drivers: Dict[str, DriverState] = {}
        self.rides: Dict[str, Ride] = {}
        self.notify = notifier

    def register_user(self, user_id: str, role: str):
        self.users[user_id] = User(user_id, role)
        if role == "driver":
            self.drivers[user_id] = DriverState(user_id, 0, 0)

    def update_location(self, driver_id: str, lat: float, lon: float):
        if driver_id in self.drivers:
            d = self.drivers[driver_id]; d.lat = lat; d.lon = lon

    def request_ride(self, passenger_id: str, pickup: Tuple[float,float], dropoff: Tuple[float,float]) -> Optional[Ride]:
        driver_id = self._find_nearest_driver(pickup)
        if not driver_id:
            return None
        ride = Ride(new_ride_id(), passenger_id, driver_id, pickup, dropoff, status="driver_assigned")
        self.rides[ride.ride_id] = ride
        self.drivers[driver_id].available = False
        self.notify.emit("driver_assigned", ride.__dict__)
        return ride

    def start_ride(self, ride_id: str):
        ride = self.rides.get(ride_id)
        if ride and ride.status == "driver_assigned":
            ride.status = "in_progress"
            self.notify.emit("ride_started", ride.__dict__)

    def complete_ride(self, ride_id: str, distance_km: float, duration_min: float, surge: float = 1.0) -> Optional[float]:
        ride = self.rides.get(ride_id)
        if ride and ride.status == "in_progress":
            ride.status = "completed"
            ride.fare = self._calc_fare(distance_km, duration_min, surge)
            self.drivers[ride.driver_id].available = True
            self.notify.emit("ride_completed", ride.__dict__)
            return ride.fare
        return None

    def _find_nearest_driver(self, pickup):
        lat, lon = pickup
        best = None; best_dist = float("inf")
        for d in self.drivers.values():
            if not d.available: continue
            dist = haversine(lat, lon, d.lat, d.lon)
            if dist < best_dist:
                best_dist, best = dist, d.user_id
        return best

    @staticmethod
    def _calc_fare(distance_km, duration_min, surge):
        base = 2.0; per_km = 1.2; per_min = 0.25
        return round((base + distance_km*per_km + duration_min*per_min) * surge, 2)
