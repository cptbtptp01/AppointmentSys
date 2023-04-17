
from appt_AppointmentDiary import AppointmentDiary

class User:
    """...
    """
    # a class variable to store all the user name
    all_users = set()

    def __init__(self, f_name:str, l_name:str) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.appointment_diary = AppointmentDiary()
    
    def __str__(self):
        return f"{self.f_name}" if not self.l_name else f"{self.f_name} {self.l_name}"

    def __hash__(self) -> int:
        return hash((self.f_name, self.l_name))

    def __eq__(self, other:'User') -> bool:
        return self.f_name == other.f_name and self.l_name == other.l_name
    
    @classmethod
    def get_user(cls) -> tuple:
        while True:
            username = input("Enter your Username(e.g.'XX Y'/'XX'/'XX-Y'):").split()
            if username:
                f_name = username[0]
                # grant for username without last name
                l_name = username[1] if len(username) > 1 else ""
                return f_name, l_name
            else:
                print("Username cannot be empty, please try again.")
    
    @classmethod
    def add_user(cls) -> str:
        f_name, l_name = cls.get_user()
        # check if user exists
        user = User(f_name, l_name)
        if user in cls.all_users:
            return f"Welcome back, {user}!"
        # add new user
        cls.all_users.add(user)
        return f"Welcome, {user}! Your profile has been added."
    
    @classmethod
    def check_user(cls) -> 'User' or None:
        f_name, l_name = cls.get_user()
        user = User(f_name, l_name)
        if user in cls.all_users:
            return user
        return None
    
    @classmethod
    def delete_user(cls) -> str:
        f_name, l_name = cls.get_user()
        # check if user exists
        user = User(f_name, l_name)
        user_to_delete = None
        # check if the username exists
        if user in cls.all_users:
            user_to_delete = user
        # process deletion and provide notification
        if user_to_delete:
            cls.all_users.discard(user_to_delete)
            return f"user {user_to_delete} has been deleted."
        else:
            return f"User not found."
        
    @classmethod
    def show_user(cls) -> list[str] or str:
        # a function controls return statement, without set condition to check if we have user or not
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        users = [str(user) for user in cls.all_users]
        return f"The system has {plural('users', len(cls.all_users))}.\n" + ",".join(users)
    
    class Archive:
        def cancel_appt(self) -> str:
        # TODO how to define time, cancel base on start time? 
        # TODO are we allowed to have more than one event at same time?
        date = Date.get_date()
        if date in self.dairy:
            appt_time = Time.get_time()
            for existing_appt in self.dairy[date]:
                if appt_time - existing_appt.end_time <= 0 and appt_time - existing_appt.start_time >= 0:
                    self.dairy[date].remove(existing_appt)
                    # rm the day if the day is clear after cancellation
                    if len(self.dairy[date]) == 0:
                        del self.dairy[date]
                    return f"Appointment has been cancelled."
        return f"Appointment not found."
    
    def check_appt(self) -> str:
        # allow for entering a time, if the time is between an appointment's start and end -> grant for checking
        date = Date.get_date()
        if date in self.dairy:
            check_time = Time.get_time()
            for existing_appt in self.dairy[date]:
                if check_time - existing_appt.end_time <= 0 and check_time - existing_appt.start_time >= 0:
                    return f"Appointment found on {date} between {existing_appt.start_time} to {existing_appt.end_time}."
        return f"Appointment not found."
    
    def get_appt(self) -> str:
        # allow for entering a time, if the time is between an appointment's start and end -> grant for retrieving
        date = Date.get_date()
        if date in self.dairy:
            check_time = Time.get_time()
            for existing_appt in self.dairy[date]:
                # e.start <= check <= e.end
                if check_time - existing_appt.end_time <= 0 and check_time - existing_appt.start_time >= 0:
                    return f"Appointment found on {date} between {existing_appt.start_time} to {existing_appt.end_time}:\nPurpose:{existing_appt.purpose}."
        return f"Appointment not found."
    
    def reschedule_appt(self) -> str:
        date = Date.get_date()
        if date in self.dairy:
            old_time = Time.get_time()
            for existing_appt in self.dairy[date]:
                # e.start <= check <= e.end
                if old_time - existing_appt.end_time <= 0 and old_time - existing_appt.start_time >= 0:
                    ...
        return f"No appointment found on {date}."