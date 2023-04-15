#
#
#
"""A module for managing date and time information.
This module contains the following classes:
- Date: Represents a date, including year, month, and day.
- Time: Represents a time, including hours, minutes in 24-hr format.
- ? DateTime: Represents a combination of a date and a time.
"""

import datetime

class Time:
    """
    """
    def __init__(self, hours: str, minutes: str, am_pm: str) -> None:
        self.hours = f"{hours:02d}"
        self.minutes = f"{minutes:02d}"
        self.am_pm = am_pm
    
    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes} {self.am_pm}"
    
    def __sub__(self, end) -> int:
        """Calculate the difference in mins between two Time objs
        """
        if self.am_pm == 'PM' and end.am_pm == 'PM':
            e = datetime.datetime(1, 1, 1, hour=int(self.hours)+12, minute=int(self.minutes))
            s = datetime.datetime(1, 1, 1, hour=int(end.hours)+12, minute=int(end.minutes))
        elif self.am_pm == 'PM':
            e = datetime.datetime(1, 1, 1, hour=int(self.hours)+12, minute=int(self.minutes))
            s = datetime.datetime(1, 1, 1, hour=int(end.hours), minute=int(end.minutes))
        elif end.am_pm == 'PM':
            e = datetime.datetime(1, 1, 1, hour=int(self.hours), minute=int(self.minutes))
            s = datetime.datetime(1, 1, 1, hour=int(end.hours)+12, minute=int(end.minutes))
        else:
            e = datetime.datetime(1, 1, 1, hour=int(self.hours), minute=int(self.minutes))
            s = datetime.datetime(1, 1, 1, hour=int(end.hours), minute=int(end.minutes))
        diff = (e - s).total_seconds() / 60
        return int(diff)

    @classmethod
    def get_time(cls):
        while True:
            try:
                time_str = input("Enter the time in HH:MM AM/PM format: ")
                try:
                    dt = datetime.datetime.strptime(time_str, "%I:%M %p")
                except ValueError:
                    # grant for not entering whitespace before am/pm
                    dt = datetime.datetime.strptime(time_str, "%I:%M%p")
                if dt.hour > 12:
                    hours = (dt.hour - 12)
                    minutes = dt.minute
                    am_pm = dt.strftime("%p")
                else:
                    hours = dt.hour
                    minutes = dt.minute
                    am_pm = dt.strftime("%p")
                return cls(hours, minutes, am_pm)
            except ValueError:
                print("Please try again in HH:MM AM/PM format.")


class Date:
    """YYYY-MM-DD
    """
    def __init__(self, year: int, month: int, day: str) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def get_date(cls):
        while True:
            try:
                date_str = input("Enter the date in YYYY-MM-DD format: ")
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                year = dt.year
                month = dt.month
                day = dt.day
                return cls(year, month, day)
            except ValueError:
                print("Please try again in YYYY-MM-DD format.")
