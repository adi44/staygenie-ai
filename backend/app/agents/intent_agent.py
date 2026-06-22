from typing import Optional
import re
from app.schemas.hotel_search import HotelSearchRequest


def _extract_int(value: Optional[str], default: int = 1) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def extract_hotel_search_request(user_query: str) -> HotelSearchRequest:
    q = user_query.lower()

    # heuristics-based extraction
    location_match = re.search(r"in\s+([A-Za-z ]+?)(?:,| for| next| next month|$)", user_query, re.IGNORECASE)
    location = location_match.group(1).strip() if location_match else ""

    guests_match = re.search(r"(\d+)\s*(?:adults|people|guests)", q)
    guests = _extract_int(guests_match.group(1) if guests_match else None, 1)

    nights_match = re.search(r"(\d+)\s*(?:nights|night)", q)
    nights = _extract_int(nights_match.group(1) if nights_match else None, 1)

    budget_match = re.search(r"under\s*inr\s*(\d+(?:,\d{3})*(?:\.\d+)?)", q, re.IGNORECASE)
    budget = None
    if budget_match:
        budget = float(budget_match.group(1).replace(",", ""))

    return HotelSearchRequest(
        location=location,
        check_in_date="",
        check_out_date="",
        guests=guests,
        rooms=1,
        budget_per_night=budget,
    )


