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
    def __init__(self, date, start_time, end_time, purpose: str) -> None:
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
    
    def __str__(self) -> str:
        return f"{self.date} {self.start_time} - {self.end_time}: {self.purpose}"
    
    @classmethod
    def schedule_appointment(cls, user):
        # validate user first
        user = User.check_user()
        if not user:
            return f"User not found."
        while True:
            # check conflicts
            print('Please enter the date of your appointment.')
            date = Date.get_date()
            print('Please enter your start time.')
            start_time = Time.get_time()
            print('Please enter your end time.')
            end_time = Time.get_time()
            if end_time - start_time > 0:
                if AppointmentDiary.check_conflicts(user.appointment_diary, date, start_time, end_time):
                    return f"Sorry, there is a conflict with an existing appointment. Please choose a different time."
                    # TODO - print that existing appointment
                break    
            else:
                print("End time must come after start time. Please enter the times again.")
        # continue when there is no conflict
        while True:
            purpose = input("Enter your purpose:")
            if purpose:
                purpose = purpose
                user.appointment_diary.add_appt(cls(date, start_time, end_time, purpose))
                print(user.appointment_diary)
                break
            else:
                return f"Purpose cannot be empty."
        return cls(date, start_time, end_time, purpose)

class AppointmentDiary:
    """{'date1': [Appointment(), Appointment(),...], 'date2': [.,.,.]}
    """
    def __init__(self) -> None:
        self.dairy = {}
    
    def __str__(self) -> str:
        output = ""
        for date, appointments in self.dairy.items():
            output += f"{date}:\n"
            for appt in appointments:
                output += f"{appt.start_time} - {appt.end_time} {appt.purpose}\n"
        return output

    def check_conflicts(self, date: Date, start: Time, end: Time) -> bool:
        """...
        """
        # if the day is clear, then add as a new key
        if date not in self.dairy:
            self.dairy[date] = []
            return False
        # check against existing appointments
        for existing_appt in self.dairy[date]:
            if start - existing_appt.start_time > 0 and start - existing_appt.end_time < 0:
                return True
            elif end - existing_appt.start_time > 0 and end - existing_appt.end_time < 0:
                return True
        # only return False after all appointments are checked
        return False
    
    def add_appt(self, appt:Appointment) -> None:
        if appt.date not in self.dairy:
            self.diary[appt.date] = []
        self.dairy[appt.date].append(appt)
        print("Appointment scheduled successfully:")

u = User.add_user()
print(u.appointment_diary)
Appointment.schedule_appointment(u)
Appointment.schedule_appointment(u)