from sqlalchemy import Boolean, String, Float, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Field(Base):
    __tablename__ = 'fields'
    id: Mapped[int] = mapped_column(primary_key=True,)
    name: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    district: Mapped[str] = mapped_column(String(32), index=True)
    description: Mapped[str|None] = mapped_column(Text,default=None)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    surface_type: Mapped[str] = mapped_column(String(32))
    has_lighting: Mapped[bool] = mapped_column(Boolean, default=False)
    is_paid: Mapped[bool] = mapped_column(Boolean, default=False)
    avg_rating: Mapped[float] = mapped_column(Float, default=0.0)
    review_count: Mapped[int] = mapped_column(Integer, default=0)

    check_ins: Mapped[list["CheckIn"]] = relationship(back_populates="field")
    chats: Mapped[list["Chat"]] = relationship(back_populates="field")
    reviews: Mapped[list["FieldReview"]] = relationship(back_populates="field")
    events: Mapped[list["Event"]] = relationship(back_populates="field")