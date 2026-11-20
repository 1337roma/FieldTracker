from datetime import datetime
from sqlalchemy import Text, DateTime, Integer, ForeignKey, func, UniqueConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Friendship(Base):
    __tablename__ = "friendships"

    id: Mapped[int] = mapped_column(primary_key=True)
    requester_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), index=True)
    addressee_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), index=True)
    status: Mapped[str] = mapped_column(String(20), default='pending')
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint("requester_id", "addressee_id", name="uq_friendship_pair"),)

    requester: Mapped["User"] = relationship(foreign_keys=[requester_id], back_populates="sent_friend_requests")
    addressee: Mapped["User"] = relationship(foreign_keys=[addressee_id], back_populates="received_friend_requests")


