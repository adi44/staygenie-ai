from dataclasses import dataclass
from typing import Optional
@dataclass
class HotelSearchRequest:
    location: str = ""
    check_in_date: str = ""
    check_out_date: str = ""
    guests: int = 1
    rooms: int = 1
    budget_per_night: Optional[float] = None
    hotel_rating: Optional[float] = None
    room_type: Optional[str] = None
