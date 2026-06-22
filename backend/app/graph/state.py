from typing import TypedDict
from app.schemas.hotel_search import HotelSearchRequest

from dataclasses import dataclass
from schemas.hotel_search import HotelSearchRequest


@dataclass
class HotelState:
    user_query: str
    hotel_search_request: HotelSearchRequest

