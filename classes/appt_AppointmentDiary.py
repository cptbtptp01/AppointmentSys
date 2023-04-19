# appt_AppointmentDiary.py

from classes.appt_Date import Date
from classes.appt_Time import Time
from classes.appt_Appointment import Appointment

class AppointmentDiary:
    """A class that represents an appointment diary.

    Attributes:
    diary (dict): A dictionary containing dates as keys and a list of appointments for that date as values.
    """
    def __init__(self) -> None:
        self.diary = {}
    
    def __str__(self) -> str:
        """ Nicely print user's appointment diary.
        """
        appt_diary = ""
        for date, appts in self.diary.items():
            appt_str = ""
            for appt in appts:
                appt_str += f"{appt.start_time} - {appt.end_time}: {appt.purpose}\n"
            appt_diary += f"{date.__str__()}:\n{appt_str}"
        return appt_diary
    
    def sort_diary(self) -> dict:
        """ Sort diary by the date and appointments by start time.
        Returns:
            dict (sorted)
        """
        dates = list(self.diary.keys())
        dates.sort()
        for date in dates:
            self.diary[date].sort(key=lambda appt: appt.start_time)
        self.diary = {i: self.diary[i]for i in dates}
        return self.diary

    def get_existing(self) -> list:
        """
        Checks if current date and time has an appointment.
        Returns:
            list(2 element): 
                -If there is: [date object, appointment object]
                -If date has appointments but no conflict: [date object, time object]
                -If date has no appointment: [message, date object]
        """
        date = Date.get_date()
        if date in self.diary:
            time = Time.get_time()
            for existing_appt in self.diary[date]:
                if time - existing_appt.end_time <= 0 and time - existing_appt.start_time >= 0:
                    return [date, existing_appt]
            return [date,time]
        return ["You don't have appointment on ", date]
    
    def schedule_appt(self) -> str:
        """
        Prompts the user to schedule an appointment.
        (ask date -> if date exists -> ask start time & end time -> if not conflict -> ask purpose -> store.)

        Returns:
            str: represent a corresponding message to user notifying:
                -If scheduled successfully
                -If conflicts with existing appointment
        """
        date = Date.get_date()
        while True:
            print("\nPlease enter your start time.")
            start_time = Time.get_time()
            print("\nPlease enter your end time.")
            end_time = Time.get_time()
            if end_time - start_time > 0:
                break
            else:
                print("\nEnd time must be later than start time.")
        new = Appointment(date, start_time, end_time,'')
        if date in self.diary:
            for existing_appt in self.diary[date]:
                if existing_appt.check_conflict(new):
                    return f"\nTime conflicts with existing appointment:[{existing_appt}]"
            # ask for entering purpose if no conflict
            new = Appointment.get_appt3(date, start_time, end_time)
            self.diary[date].append(new)
            self.sort_diary()
        else:
            # ask for entering purpose if no conflict
            new = Appointment.get_appt3(date, start_time, end_time)
            self.diary[date] = [new]
            self.sort_diary()
        return f"\nAppointment scheduled successfully: [{new}]"
    
    def cancel_appt(self) -> str:
        """
        Prompts the user to cancel an appointment.
        Returns:
            str: represent a corresponding message to user notifying:
                -If cancelled successfully
                -If no appointment found 
        """
        if not self.diary:
            return f"\nYou don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            self.diary[appt[0]].remove(appt[1])
            # rm the day if the day is clear after cancellation
            if len(self.diary[appt[0]]) == 0:
                del self.diary[appt[0]]
                self.sort_diary()
            return f"\nAppointment has been cancelled on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}."
        elif isinstance(appt[1], Time):
            return f"\nAppointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"\n{appt[0]}{appt[1]}."

    def check_appt(self) -> str:
        """
        Prompts the user to checking an appointment.
        Pre-condition:
            any time between the start time and end time of the scheduled appointment is allowed for checking
        Returns:
            str: represent a corresponding message to user notifying:
                -If found successfully
                -If no appointment found 
        """
        if not self.diary:
            return f"\nYou don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            return f"\nAppointment found on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}."
        elif isinstance(appt[1], Time):
            return f"\nAppointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"\n{appt[0]}{appt[1]}."
    
    def get_appt(self) -> str:
        """
        Prompts the user to retrieving an appointment purpose.
        Pre-condition:
            any time between the start time and end time of the scheduled appointment is allowed for checking
        Returns:
            str: represent a corresponding message to user notifying:
                -If found successfully, with the purpose of the appointment
                -If no appointment found 
        """
        if not self.diary:
            return f"\nYou don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            return f"\nAppointment found:\n[{appt[0]} between {appt[1].start_time} to {appt[1].end_time}: {appt[1].purpose}]"
        elif isinstance(appt[1], Time):
            return f"\nAppointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"\n{appt[0]}{appt[1]}."
    
    def reschedule_appt(self) -> str:
        """
        Prompts the user to rescheduling an appointment.
        Pre-condition:
            any time between the start time and end time of the scheduled appointment is allowed for checking
        Returns:
            str: represent a corresponding message to user notifying:
                -If rescheduled successfully
                -If no appointment found 
        """
        if not self.diary:
            return f"\nYou don't have any appointment in the system."
        try:
            appt = self.get_existing()
            # if the date and time user entered does hold an appointment
            if isinstance(appt[1], Appointment):
                # store, save back if conflict
                old_purpose = appt[1].purpose
                old_start_time = appt[1].start_time
                old_end_time = appt[1].end_time
                self.diary[appt[0]].remove(appt[1])
                print(f"\nYou have appointment on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}.\nWhat new time would you like to reschedule?")
                new_date = Date.get_date()
                new = Appointment.get_appt2(new_date, old_purpose)
                if new_date in self.diary:
                    for existing_appt in self.diary[new_date]:
                        if existing_appt.check_conflict(new):
                            # keep appointment
                            old = Appointment(appt[0], old_start_time, old_end_time, old_purpose)
                            self.diary[appt[0]].append(old)
                            return f"\nAppointment conflicts with existing appointment: [{existing_appt}]"
                    # store the rescheduled appointment to the diary
                    self.diary[new_date].append(new)
                    self.sort_diary()
                else:
                    # new date is clear
                    # store the rescheduled appointment to the diary
                    self.diary[new_date] = [new]
                    self.sort_diary()
                # check if after reschedule, the old date is clear, if so, delete
                if len(self.diary[appt[0]]) == 0:
                    del self.diary[appt[0]]
                return f"\nAppointment rescheduled successfully on {new_date} between {new.start_time} to {new.end_time}."
            # if the date holds appointments but the time user entered is clear
            elif isinstance(appt[1], Time):
                return f"\nAppointment not found on {appt[0]} at {appt[1]}."
            # if the day is clear
            else:
                return f"\n{appt[0]}{appt[1]}."
        except TypeError: # FIXME - not sure if here need try-except block
            print("\n(error message from reschedule method) Invalid Input, please try again.")
    
def schedule_appt2(self) -> str:
        """
        (for record, not used in the main module.)
        Checks if current date and time has an appointment.
        (ask date -> if date exists -> ask start time -> if start time not conflict -> ask end time -> if end time not conflict -> ask purpose -> store.)
        >>> user friendly or not??
        Returns:
            str
        """
        date = Date.get_date()
        while True:
            if date in self.diary:
                # get start_time
                print("\nPlease enter your start time.")
                s_time = Time.get_time()
                for existing_appt in self.diary[date]:
                    if s_time - existing_appt.end_time <= 0 and s_time - existing_appt.start_time >= 0:
                        return f"An existing appointment is already at {s_time}."
                    # if start time is not conflict, get end_time for checking:
                    print("Please enter your end time.")
                    e_time = Time.get_time()
                    if e_time - existing_appt.end_time <= 0 and e_time - existing_appt.start_time >= 0:
                        return f"An existing appointment is already at {s_time}."
                # if no conflict, ask for purpose and store in the diary
                if e_time - s_time > 0:
                    new = Appointment.get_appt3(date,s_time,e_time)
                    self.diary[date].append(new)
                    return f"Appointment scheduled successfully: [{new}]\n"
            else:
                # if the date has no appointment, ask for start time, end_time, purpose
                new = Appointment.get_appt(date)
                self.diary[date] = [new]
                return f"Appointment scheduled successfully: [{new}]\n"
