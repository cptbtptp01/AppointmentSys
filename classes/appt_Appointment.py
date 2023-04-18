# appt_Appointment.py
# huiru yang (yang.huir@northeastern.edu)
# April 17 2023

from classes.appt_Date import Date
from classes.appt_Time import Time

class Appointment:
    """A module represents an appointment with a date, start time, end time, and purpose.
    Attributes:
        date (Date): The date of the appointment.
        start_time (Time): The start time of the appointment.
        end_time (Time): The end time of the appointment.
        purpose (str): The purpose of the appointment.
    """ 
    def __init__(self, date: Date, start_time: Time, end_time: Time, purpose: str) -> None:
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Appointment instance.
        """
        return f"{self.date} {self.start_time} - {self.end_time}: {self.purpose}"
    
    def check_conflict(self, other:'Appointment') -> bool:
        """
        Checks whether the current Appointment instance conflicts with another Appointment instance.
        Args:
            other (Appointment): The other Appointment instance to check for conflicts.
        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        if other.end_time - self.start_time < 0 or other.start_time - self.end_time > 0:
            return False
        return True
    
    @classmethod
    def get_appt(cls, date: Date) -> 'Appointment':
        """
        Creates a new Appointment instance by prompting the user for start time, end time, and purpose.
        Args:
            date (Date): The date of the appointment.
        Returns:
            Appointment: The new Appointment instance.
        """
        while True:
            print("\nPlease enter your start time.")
            start_time = Time.get_time()
            print("\nPlease enter your end time.")
            end_time = Time.get_time()
            if end_time - start_time > 0:
                break
            else:
                print("\nEnd time must be later than start time.")
        while True:
            try:   
                purpose = input("\nEnter your purpose:")
                if purpose:
                    return cls(date, start_time, end_time, purpose)
            except ValueError:
                print('\nPurpose cannot be empty.')

    @classmethod
    def get_appt2(cls, date: Date, purpose:str) -> 'Appointment':
        """
        Creates a new Appointment instance by prompting the user for start time and end time.
        Args:
            date (Date): The date of the appointment.
            purpose (str): The purpose of the appointment.
        Returns:
            Appointment: The new Appointment instance.
        """
        while True:
            print("\nPlease enter your start time.")
            start_time = Time.get_time()
            print("\nPlease enter your end time.")
            end_time = Time.get_time()
            if end_time - start_time > 0:
                break
            else:
                print("\nEnd time must be later than start time.")
        return cls(date, start_time, end_time, purpose)

    @classmethod
    def get_appt3(cls, date: Date, start_time: Time, end_time: Time) -> 'Appointment':
        """
        Creates a new Appointment instance by prompting the user for purpose.
        Args:
            date (Date): The date of the appointment.
            start_time (Time): The start time of the appointment.
            end_time (Time): The end time of the appointment.
        Returns:
            Appointment: The new Appointment instance.
        """
        while True:
            try:   
                purpose = input("\nEnter your purpose:")
                if purpose:
                    return cls(date, start_time, end_time, purpose)
            except ValueError:
                print('\nPurpose cannot be empty.')