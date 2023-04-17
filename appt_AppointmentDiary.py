from appt_Date import Date
from appt_Time import Time
from appt_Appointment import Appointment

class AppointmentDiary:
    """
    """
    def __init__(self) -> None:
        self.diary = {}
    
    def __str__(self) -> str:
        appt_diary = ""
        for date, appts in self.diary.items():
            appt_str = ""
            for appt in appts:
                appt_str += f"{appt.start_time} - {appt.end_time}: {appt.purpose}\n"
            appt_diary += f"{date.__str__()}:\n{appt_str}"
        return appt_diary
    
    def get_existing(self) -> list:
        date = Date.get_date()
        if date in self.diary:
            time = Time.get_time()
            for existing_appt in self.diary[date]:
                if time - existing_appt.end_time <= 0 and time - existing_appt.start_time >= 0:
                    return [date, existing_appt]
            return [date,time]
        return ["You don't have appointment on ", date]
    
    def schedule_appt(self) -> str:
        date = Date.get_date()
        while True:
            print("Please enter your start time.")
            start_time = Time.get_time()
            print("Please enter your end time.")
            end_time = Time.get_time()
            if end_time - start_time > 0:
                break
            else:
                print("End time must be later than start time.")
        new = Appointment(date, start_time, end_time,'')
        if date in self.diary:
            for existing_appt in self.diary[date]:
                if existing_appt.check_conflict(new):
                    return f"Time conflicts with existing appointment:[{existing_appt}]"
            # ask for entering input if no conflict
            new = Appointment.get_appt3(date, start_time, end_time)
            self.diary[date].append(new)
        else:
            # ask for entering input if no conflict
            new = Appointment.get_appt3(date, start_time, end_time)
            self.diary[date] = [new]
        return f"Appointment scheduled successfully: [{new}]\n"
    
    def cancel_appt(self) -> str:
        if not self.diary:
            return f"You don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            self.diary[appt[0]].remove(appt[1])
            # rm the day if the day is clear after cancellation
            if len(self.diary[appt[0]]) == 0:
                del self.diary[appt[0]]
            return f"Appointment has been cancelled."
        elif isinstance(appt[1], Time):
            return f"Appointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"{appt[0]}{appt[1]}."

    def check_appt(self) -> str:
        # allow for entering a time, if the time is between an appointment's start and end -> grant for checking
        if not self.diary:
            return f"You don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            return f"Appointment found on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}."
        elif isinstance(appt[1], Time):
            return f"Appointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"{appt[0]}{appt[1]}."
    
    def get_appt(self) -> str:
        # allow for entering a time, if the time is between an appointment's start and end -> grant for retrieving
        if not self.diary:
            return f"You don't have any appointment in the system."
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            return f"Appointment found on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}: {appt[1].purpose}."
        elif isinstance(appt[1], Time):
            return f"Appointment not found on {appt[0]} at {appt[1]}."
        else:
            return f"{appt[0]}{appt[1]}."
    
    def reschedule_appt(self) -> str:
        if not self.diary:
            return f"You don't have any appointment in the system."
        try:
            appt = self.get_existing()
            # if the date and time user entered does hold an appointment
            if isinstance(appt[1], Appointment):
                # store, save back if conflict
                old_purpose = appt[1].purpose
                old_start_time = appt[1].start_time
                old_end_time = appt[1].end_time
                self.diary[appt[0]].remove(appt[1])
                print(f"You have appointment on {appt[0]} between {appt[1].start_time} to {appt[1].end_time}. What new time would you like to reschedule?")
                new_date = Date.get_date()
                new = Appointment.get_appt2(new_date, old_purpose)
                if new_date in self.diary:
                    for existing_appt in self.diary[new_date]:
                        if existing_appt.check_conflict(new):
                            # keep appointment
                            old = Appointment(appt[0], old_start_time, old_end_time, old_purpose)
                            self.diary[appt[0]].append(old)
                            return f"Appointment conflicts with existing appointment: [{existing_appt}]"
                    self.diary[new_date].append(new)
                else:
                    self.diary[new_date] = [new]
                # check if after reschedule, the old date is clear
                if len(self.diary[appt[0]]) == 0:
                    del self.diary[appt[0]]
                return f"Appointment rescheduled successfully on {new_date} between {new.start_time} to {new.end_time}."
            # if the date holds appointments but the time user entered is clear
            elif isinstance(appt[1], Time):
                return f"Appointment not found on {appt[0]} at {appt[1]}."
            # if the day is clear
            else:
                return f"{appt[0]}{appt[1]}."
        except TypeError: # FIXME - not sure if here need try-except block
            print("(error message from reschedule method) Invalid Input, please try again.")
    
    def schedule2(self) -> str: 
        # FIXME another try but failed to check end_time
        appt = self.get_existing()
        if isinstance(appt[1], Appointment):
            return f"Appointment conflicts with existing appointment:\n{appt[1]}"
        elif isinstance(appt[1], Time):
            # the time we got is the start time
            # FIXME pass checking if end_time is conflict
            new = Appointment.get_appt2(appt[0],appt[1])
            self.diary[appt[0]].append(new)
        else:
            # the day is clear
            new = Appointment.get_appt(appt[1])
            self.diary[appt[1]] = [new]
        return f"Appointment scheduled successfully: [{new}]\n"