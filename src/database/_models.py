from datetime import datetime
import enum


from sqlalchemy import BIGINT, Integer, TIMESTAMP, Float, String, func
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy import Enum

Base = declarative_base()


class BetType(Enum):
    up = 'UP'
    down = 'DOWN'


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    balance: Mapped[float | None] = mapped_column(Float)
    volume: Mapped[float | None] = mapped_column(Float)
    ref_id: Mapped[int | None] = mapped_column(BIGINT)


class Wallet(Base):
    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    address: Mapped[str] = mapped_column(String(64))
    seed: Mapped[str] = mapped_column(String(64))


class Bet(Base):
    __tablename__ = 'bets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    start: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    end: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    bet_type: Mapped[enum] = mapped_column(Enum(BetType))
    profit: Mapped[float] = mapped_column(Float)