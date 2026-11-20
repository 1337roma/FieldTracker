from datetime import datetime
from sqlalchemy import Text, DateTime, Integer, ForeignKey, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class FieldReview(Base):
    __tablename__ = "field_reviews"
    id: Mapped[int] = mapped_column(primary_key=True)
    field_id: Mapped[int] = mapped_column(ForeignKey('fields.id', ondelete='CASCADE'), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str|None] = mapped_column(Text, default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("user_id", "field_id", name="uq_user_field_review"),
    )

    field: Mapped["Field"] = relationship(back_populates="reviews")
    user: Mapped["User"] = relationship(back_populates="reviews")