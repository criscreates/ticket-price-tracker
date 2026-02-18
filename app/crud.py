from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas


def sync_event_price(db: Session, event_data: schemas.EventData):
    """
    Given the data for an event and a DB session,
    check if the Event exists. If it doesn't, a new Event is created.
    A new PriceHistory record is always created,
    to add new data for the Event.
    """

    stmt = select(models.Event).where(models.Event.id == event_data.id)
