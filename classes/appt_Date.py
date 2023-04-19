# appt_Date.py

import datetime

class Date:
    """A module for representing a date using the YYYY-MM-DD format.
    Attributes:
        year(int): represents year (e.g. 2023)
        month(int): represents month (1-12)
        day(int): represents day of the month (1-31)
    """
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
    
    def __hash__(self) -> int:
        return hash((self.year,self.month,self.day))
    
    def __eq__(self, other: 'Date') -> bool:
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other: 'Date') -> bool:
        if self.year != other.year:
            return self.year < other.year
        elif self.month != other.month:
            return self.month < other.month
        else:
            return self.day < other.day

    @classmethod
    def get_date(cls):
        """Prompt the user to enter a date in YYYY-MM-DD format.
        The user is prompted repeatedly until a valid date is entered.
        Returns:
        a new Date object representing the entered date
        """
        while True:
            try:
                date_str = input("\nEnter the date in YYYY-MM-DD format: ")
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                year = dt.year
                month = dt.month
                day = dt.day
                return cls(year, month, day)
            except ValueError:
                print("\nPlease try again in YYYY-MM-DD format.")
