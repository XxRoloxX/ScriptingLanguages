from typing import List
from sqlalchemy import ForeignKey
from datetime import datetime as DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Stations(Base):
    __tablename__ = "stations"
    station_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    station_name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f"Station(station_id={self.station_id!r}, station_name={self.station_name})"
    
    def to_tupe(self):
        return self.station_id, self.station_name

class Rentals(Base):
    __tablename__ = "rentals"
    rental_id: Mapped[str] = mapped_column(primary_key=True)
    bike_number: Mapped[str]
    start_time: Mapped["DateTime"]
    end_time: Mapped["DateTime"]
    duration: Mapped[int]
    rental_station_id: Mapped[int] = mapped_column(ForeignKey("stations.station_id"))
    return_station_id: Mapped[int] = mapped_column(ForeignKey("stations.station_id"))
    rental_station: Mapped["Stations"] = relationship(foreign_keys=[rental_station_id])
    return_station: Mapped["Stations"] = relationship(foreign_keys=[return_station_id])


    def __repr__(self) -> str:
        return f"Rental(rental_id={self.rental_id!r},bike_number={self.bike_number!r}, start_time={self.start_time!r}, end_time={self.end_time!r}, rental_station={self.rental_station!r}, return_station={self.return_station!r})"


