from datetime import date
from sqlalchemy import Date, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Temperature(Base):
    __tablename__ = "temperature"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[date | None] = mapped_column(Date, nullable=True)
    avgtemp_c: Mapped[float | None] = mapped_column(Float, nullable=True)
    mintemp_c: Mapped[float | None] = mapped_column(Float, nullable=True)
    maxtemp_c: Mapped[float | None] = mapped_column(Float, nullable=True)
  