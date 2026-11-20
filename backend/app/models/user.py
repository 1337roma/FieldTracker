from datetime import datetime
from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str|None] = mapped_column(String(255), default=None)
    avatar_url: Mapped[str|None] = mapped_column(String(255), default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    check_ins: Mapped[list["CheckIn"]] = relationship(back_populates="user")
    messages: Mapped[list["Message"]] = relationship(back_populates="sender")
    chat_members: Mapped[list["ChatMember"]] = relationship(back_populates="user")

    reviews: Mapped[list["FieldReview"]] = relationship(back_populates="user")
    created_events: Mapped[list["Event"]] = relationship(back_populates="creator")
    event_participants: Mapped[list["EventParticipant"]] = relationship(back_populates="user")
    sent_friend_requests: Mapped[list["Friendship"]] = relationship(foreign_keys="Friendship.requester_id", back_populates="requester")
    received_friend_requests: Mapped[list["Friendship"]] = relationship(foreign_keys="Friendship.addressee_id", back_populates="addressee")
