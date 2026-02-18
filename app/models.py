from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, func
from typing import Optional, List
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)

    event_date: Mapped[Optional[str]] = mapped_column(String)
    venue_name: Mapped[Optional[str]] = mapped_column(String)
    venue_city: Mapped[Optional[str]] = mapped_column(String)

    price_history: Mapped[List["PriceHistory"]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )


class PriceHistory(Base):
    __tablename__ = "price_history"

    min_price: Mapped[Optional[float]]
    max_price: Mapped[Optional[float]]
    currency: Mapped[str] = mapped_column(String, default="USD")

    recorded_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    event: Mapped["Event"] = relationship(back_populates="price_history")
