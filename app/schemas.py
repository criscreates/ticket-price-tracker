from pydantic import BaseModel, ConfigDict
from typing import Optional


class PriceRecordBase(BaseModel):
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    currency: str = "USD"


class EventBase(BaseModel):
    id: str  # Ticketmaster event ID
    name: str
    url: str
    event_date: Optional[str] = None  # TODO: want to make this more robust later
    venue_name: Optional[str] = None
    venue_city: Optional[str] = None


class EventData(EventBase):
    current_price: PriceRecordBase

    model_config = ConfigDict(from_attributes=True)
