from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine, Float
from sqlalchemy.orm import sessionmaker, Session, relationship, declarative_base, Mapped, Session, mapped_column
from pydantic import BaseModel

Base = declarative_base()

class LeaderboardEntry(Base):
    __tablename__ = "leaderboard_entry"

    entry_id: Mapped[int] = mapped_column(Integer, Sequence('entry_id_seq'), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey=True, nullable=False) # foreign key to users table

    daily_streak: Mapped[int] = mapped_column(Integer, default=0)  # current streak of dailies completed
    longest_daily_streak:  Mapped[int] = mapped_column(Integer)  # highest daily streak ever recorded
    average_daily_guesses:  Mapped[int] = mapped_column(Integer)
    average_daily_time: Mapped[float] = mapped_column(Float)  # average time to complete the daily in seconds
    longest_survival_streak: Mapped[int] = mapped_column(Integer)


class Leaderboard:

    def __init__(self, session: Session):
        self.session = session

    async def create_user_entry(user_id: int):
        """
        Creates a new LeaderboardEntry for the given user,
        if one doesn't already exit
        """
        pass

    async def update_user_entry(user_id: int):
        """
        Updates a user's leaderboard stats based on their statistics
        from StatisticsRepository
        """
        pass

    async def get_entry(user_id: int) -> LeaderboardEntry:
        """
        Get a leaderboard entry by user id
        """
        pass

    async def get_250_entries(position: int) -> list[LeaderboardEntry]:
        """
        Get 250 leaderboard entries from the given position (from the top)
        """
        pass

    async def get_friend_entries(user_id: int) -> list[LeaderboardEntry]:
        """
        Get all leaderboard entries for the given user's friends only
        (including the given user)
        """
        pass

class LeaderboardEntrySchema(BaseModel):
    id: int
    user_id: int
    daily_streak: int
    longest_daily_streak: int
    average_daily_guesses: int
    average_daily_time: float
    longest_survival_streak: int

    class Config:
        orm_mode = True
