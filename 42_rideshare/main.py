#!/usr/bin/env python
# main.py
from .notify import Notifier
from .ride_service import RideService

def run():
    rs = RideService(Notifier())
    rs.register_user("d1","driver"); rs.update_location("d1", 12.9, 77.6)
    rs.register_user("p1","passenger")
    ride = rs.request_ride("p1", (12.91,77.60), (12.95,77.64))
    print("Assigned:", ride)
    if ride:
        rs.start_ride(ride.ride_id)
        fare = rs.complete_ride(ride.ride_id, 8, 18, surge=1.3)
        print("Fare:", fare)

if __name__ == "__main__":
    run()
