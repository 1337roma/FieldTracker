from datetime import datetime
from sqlalchemy import Text, DateTime, Integer, ForeignKey, func, UniqueConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), index = True)
    field_id: Mapped[int] = mapped_column(ForeignKey('fields.id', ondelete='CASCADE'), index = True)
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str|None] = mapped_column(Text, default=None)
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    max_players: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20), default="open")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    creator: Mapped["User"] = relationship(back_populates="created_events")
    field: Mapped["Field"] = relationship(back_populates="events")
    participants: Mapped[list["EventParticipant"]] = relationship(back_populates="event")

class EventParticipant(Base):
    __tablename__ = 'event_participants'

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id" ,ondelete='CASCADE'), index = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), index = True)
    team_side: Mapped[str| None] = mapped_column(String(120), default=None)
    joined_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("event_id", "user_id", name="uq_event_user_participant"),
    )

    event: Mapped["Event"] = relationship(back_populates="participants")
    user: Mapped["User"] = relationship(back_populates="event_participants")