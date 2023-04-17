# appt_Time.py
# huiru yang (yang.huir@northeastern.edu)
# April 17 2023
"""A module for representing a time, including hours, minutes in 12-hr format.
Attributes:
    hour(str): a string represents hour
    minutes(str):a string represents minutes
    am_pm(str): either 'AM' or 'PM'
"""

import datetime

class Time:
    """Create a new Time object with the specified hours, minutes, and AM/PM suffix.
    Attributes:
        hours: a string representing the hour (1-12)
        minutes: a string representing the minute (0-59)
        am_pm: either 'AM' or 'PM'
    """
    def __init__(self, hours: str, minutes: str, am_pm: str) -> None:
        self.hours = f"{hours:02d}"
        self.minutes = f"{minutes:02d}"
        self.am_pm = am_pm
    
    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes} {self.am_pm}"
    
    def __hash__(self) -> int:
        return ((self.hours, self.minutes, self.am_pm))
    
    def __eq__(self, other) -> bool:
        return self.hours == other.hours and self.minutes == other.minutes and self.am_pm == other.am_pm
    
    def __sub__(self, other: 'Time') -> int:
        """Calculate the time difference between two Time objects, in minutes.
        Both Time objects are first converted to 24-hour format to facilitate the calculation.
        Args:
            other: a Time object representing the other time to compare against
        Returns:
            int: representing the difference in minutes between the two times
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
        """Prompt the user to enter a time in HH:MM AM/PM format, and return a new Time object.
        The user is prompted repeatedly until a valid time is entered.
        Returns:
            a new Time object representing the entered time
        """
        while True:
            try:
                time_str = input("Enter the time in HH:MM AM/PM/am/pm or HH:MMAM/PM/am/pm or H:M AM/PM/am/pm or H:MAM/PM/am/pm format: ")
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
                print("Please try again in HH:MM AM/PM/am/pm or HH:MMAM/PM/am/pm or H:M AM/PM/am/pm or H:MAM/PM/am/pm format.")