import os
import requests
from .config import settings
from typing import Optional
from http import HTTPStatus
from . import schemas


def fetch_ticketmaster_event(event_id: str) -> Optional[schemas.EventData]:
    """
    Call Ticketmaster API, extract nested data for a specific event,
    and return a clean Pydantic EventData object.
    """
    url = f"https://app.ticketmaster.com/discovery/v2/events/{event_id}.json"
    params = {"apikey": settings.TM_API_KEY}

    response = requests.get(url, params=params)
    if response.status_code != HTTPStatus.OK.value:
        return None

    data: dict = response.json()

    venues = data.get("_embedded", {}).get("venues, [{}]")
    venue: dict = venues[0]

    prices: dict = data.get("priceRanges", [{}])[0]

    return schemas.EventData(
        id=data.get("id"),
        name=data.get("name"),
        url=data.get("url"),
        event_date=data.get("dates", {}).get("start", {}).get("dateTime"),
        venue_name=venue.get("name"),
        venue_city=venue.get("city", {}).get("name"),
        current_price=schemas.PriceRecordBase(
            min_price=prices.get("min"),
            max_price=prices.get("max"),
            currency=prices.get("currency", "USD"),
        ),
    )
