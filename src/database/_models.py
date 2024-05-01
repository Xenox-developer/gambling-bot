from datetime import datetime

from sqlalchemy import BIGINT, TIMESTAMP, String, func, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()


class BetType(Enum):
    up = 'UP'
    down = 'DOWN'


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    balance: Mapped[float] = mapped_column(server_default=text('0'))
    volume: Mapped[float] = mapped_column(server_default=text('0'))
    ref_id: Mapped[int | None] = mapped_column(BIGINT)


class Wallet(Base):
    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)
    address: Mapped[str] = mapped_column(String(48))
    seed: Mapped[list[str] | None] = mapped_column(ARRAY(String))


class Bet(Base):
    __tablename__ = 'bets'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)
    start: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    end: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    bet_type: Mapped[BetType | None]
    profit: Mapped[float]
