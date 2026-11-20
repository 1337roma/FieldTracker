from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CheckIn(Base):
    __tablename__ = "check_ins"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    field_id: Mapped[int] = mapped_column(ForeignKey("fields.id", ondelete="CASCADE"), index=True)
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    planned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    expired_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    notes: Mapped[str|None] = mapped_column(Text, default=None)

    user: Mapped["User"] = relationship(back_populates="check_ins")
    field: Mapped["Field"] = relationship(back_populates="check_ins")