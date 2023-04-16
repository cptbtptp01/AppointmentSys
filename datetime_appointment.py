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
    
    def __sub__(self, other: 'Time') -> int:
        """Convert to 24-hr format.
            Calculate the difference in mins between two Time objs
        """
        if self.am_pm == 'PM' and int(self.hours) < 12:
            hour = int(self.hours) + 12
        else:
            hour = int(self.hours)
        if other.am_pm == 'PM' and int(other.hours) < 12:
            other_hour = int(other.hours) + 12
        else:
            other_hour = int(other.hours)
        if hour == 12 and self.am_pm == 'AM':
            hour = 0
        if other_hour == 12 and other.am_pm == 'AM':
            other_hour = 0
        diff = (hour - other_hour)*60 + (int(self.minutes) - int(other.minutes))
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
                hours = dt.hour
                minutes = dt.minute
                am_pm = dt.strftime("%p")
                if am_pm == 'PM' and hours > 12:
                    hours -= 12
                return cls(hours, minutes, am_pm)
            except ValueError:
                print("Please try again in HH:MM AM/PM format.")


class Date:
    """YYYY-MM-DD
    """
    def __init__(self, year: int, month: int, day: int) -> None:
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