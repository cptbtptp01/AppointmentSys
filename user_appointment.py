#
#
#

"""
"""

from datetime_appointment import Time, Date

class User:
    """...
    """
    # a class variable to store all the user name
    all_users = []

    def __init__(self, f_name:str, l_name:str) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.appointment_diary = AppointmentDiary()
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    @classmethod
    def add_user(cls) -> str:
        while True:
            username = input("Enter your Username(accept full name and first name only):").split()
            if username:
                f_name = username[0]
                # grant for username without last name
                l_name = username[1] if len(username) > 1 else ""
                break
            else:
                print("Username cannot be empty, please try again.")
        # check if user exists
        for user in cls.all_users:
            if user.f_name == f_name and user.l_name == l_name:
                return f"Welcome back, {user}!"
        # add new user
        new_user = cls(f_name, l_name)
        cls.all_users.append(new_user)
        return f"Welcome, {new_user}! Your profile has been added."
    
    @classmethod
    def check_user(cls):
        while True:
            username = input("Enter your Username(accept full name and first name only):").split()
            if username:
                f_name = username[0]
                # grant for username without last name
                l_name = username[1] if len(username) > 1 else ""
                break
            else:
                print("Username cannot be empty, please try again.")
        for user in cls.all_users:
            if user.f_name == f_name and user.l_name == l_name:
                return user
        return None
    
    @classmethod
    def delete_user(cls) -> str:
        while True:
            username = input("Enter the Full Name of the user you want to delete:").split()
            if username:
                f_name = username[0]
                # grant for username without last name
                l_name = username[1] if len(username) > 1 else ""
                break
            else:
                print("Username cannot be empty, please try again.")
        user_to_delete = None
        # check if the username exists
        for user in cls.all_users:
            if user.f_name == f_name and user.l_name == l_name:
                user_to_delete = user
                break
        # process deletion and provide notification
        if user_to_delete:
            cls.all_users.remove(user_to_delete)
            return f"user {user_to_delete} has been deleted."
        else:
            return f"User not found."
        
    @classmethod
    def show_user(cls) -> list[str] or str:
        # a function controls return statement, without set condition to check if we have user or not
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        users = [str(user) for user in cls.all_users]
        return f"The system has {plural('users', len(cls.all_users))}.\n" + ",".join(users)
    
    #TODO: get_diary() return user.appointment_diary
    #TODO: get_appointment

class Appointment:
    """ TODO: schedule, cancel, check, retrieve, reschedule
        TODO: check conflict
    """
    def __init__(self, date: Date, start_time: Time, end_time: Time, purpose: str) -> None:
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
    
    def __str__(self) -> str:
        return f"{self.date} {self.start_time} - {self.end_time}: {self.purpose}"
    
    def check_conflict(self, other:'Appointment') -> bool:
        # return True if there is conflicts
        if other.end_time - self.start_time < 0 or other.start_time - self.end_time > 0:
            return False
        return True
    
    @classmethod
    def add_appt(cls, date: Date) -> 'Appointment':
        while True:
            print("Please enter your start time.")
            start_time = Time.get_time()
            print("Please enter your end time.")
            end_time = Time.get_time()
            if end_time - start_time > 0:
                break
            else:
                print("End time must be later than start time.")
        while True:
            try:   
                purpose = input("Enter your purpose:")
                if purpose:
                    return cls(date, start_time, end_time, purpose)
            except ValueError:
                print('Purpose cannot be empty.')

class AppointmentDiary:
    """{'date1': [Appointment(), Appointment(),...], 'date2': [.,.,.]}
    """
    def __init__(self) -> None:
        self.dairy = {}
    
    def __str__(self) -> str:
        appt_diary = ""
        for date, appts in self.dairy.items():
            appt_str = ""
            for appt in appts:
                appt_str += f"{appt.start_time} - {appt.end_time}: {appt.purpose}\n"
            appt_diary += f"{date.__str__()}:\n{appt_str}"
        return appt_diary

    def schedule_appt(self) -> str:
        date_obj = Date.get_date()
        date_key = date_obj.__str__()
        new = Appointment.add_appt(date_obj)
        if date_key in self.dairy:
            for existing_appt in self.dairy[date_key]:
                if existing_appt.check_conflict(new):
                    return f"Appointment conflicts with existing appointment:\n{existing_appt}"
            self.dairy[date_key].append(new)
            d = AppointmentDiary()
        else:
            self.dairy[date_key] = [new]
            d = AppointmentDiary()
        return f"Appointment scheduled successfully.\n {d}"
    
    def cancel_appt(self) -> str:
        # TODO how to define time, cancel base on start time? are we allowed to have more than one event at same time?
        date_obj = Date.get_date()
        date_key = date_obj.__str__()
        if date_key in self.dairy:
            appt_time_str = Time.get_time().__str__()
            for existing_appt in self.dairy[date_key]:
                if existing_appt.start_time.__str__() == appt_time_str:
                    self.dairy[date_key].remove(existing_appt)
                    print(self.dairy) # TODO memory location
                    return f"Appointment has been cancelled."
        return f"Appointment not found."

    
    def check_appt(self) -> str:
        # allow for entering a time, if the time is between an appointment's start and end -> grant
        date_obj = Date.get_date()
        date_key = date_obj.__str__()
        if date_key in self.dairy:
            check_time = Time.get_time()
            for existing_appt in self.dairy[date_key]:
                # e.start <= check <= e.end
                if check_time - existing_appt.end_time <= 0 and check_time - existing_appt.start_time >= 0:
                    return f"Found. You have appointment during {existing_appt.start_time} - {existing_appt.end_time}:\nPurpose:{existing_appt.purpose}."
        return f"Appointment not found."