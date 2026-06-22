from app.graph.state import HotelState
from app.agents.intent_agent import extract_hotel_search_request

def handle_query(user_query: str) -> HotelState:
    """Simple handler that converts a user query into a HotelState using the intent parser.

    This avoids external graph dependencies and is suitable for tests and early development.
    """
    hotel_search_request = extract_hotel_search_request(user_query)
    return HotelState(user_query=user_query, hotel_search_request=hotel_search_request)
