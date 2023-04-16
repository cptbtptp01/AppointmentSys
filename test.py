from datetime import datetime, timedelta
import string

class Time:
    def __init__(self, hour, minutes, am_pm):
        self.hour = hour
        self.minutes = minutes
        self.am_pm = am_pm
    
    def to_24_hour_format(self):
        if self.am_pm.lower() == 'am':
            if self.hour == 12:
                self.hour = 0
        elif self.am_pm.lower() == 'pm':
            if self.hour != 12:
                self.hour += 12
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minutes:02d} {self.am_pm.upper()}"
    
    def __sub__(self, other):
        t1 = datetime(2023, 1, 1, self.hour, self.minutes)
        t2 = datetime(2023, 1, 1, other.hour, other.minutes)
        return (t1 - t2).total_seconds() / 60

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class User:
    # a class variable to store all the user name TODO: what if user enter without lastname
    all_users = []
    def __init__(self, f_name:str, l_name:str) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.appointment_diary = []
        # verify if user exists
        if (f_name, l_name) not in [(u.f_name, u.l_name) for u in User.all_users]:
            User.all_users.append(self)
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    @classmethod
    def get_user(cls) -> str:
        # split username into a list item
        username = input("Enter your Full Name:").upper().split()
        f_name = username[0]
        # grant for username without last name
        l_name = username[1] if len(username) > 1 else ""
        new_user = cls(f_name, l_name)
        # notification
        if new_user in cls.all_users:
            return f"{new_user} already exists."
        else:
            return f"{new_user} has been added."
        
    @classmethod
    def delete_user(cls) -> None:
        username = input("Enter the Full Name of the user you want to delete:").upper().split()
        f_name = username[0]
        # grant for username without last name
        l_name = username[1] if len(username) > 1 else ""
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
            return f"user not found."
        
    @classmethod
    def show_user(cls) -> list:
        if cls.all_users:
            return [str(user) for user in cls.all_users]
        else:
            return f"There is not users in the system yet."
        
class Appointment:

    def schedule_appointment(self, date, start_time, end_time, purpose):
        start_datetime = datetime(date.year, date.month, date.day, start_time.hour, start_time.minutes)
        end_datetime = datetime(date.year, date.month, date.day, end_time.hour, end_time.minutes)
        
        for appt in self.appointment_diary:
            if start_datetime < appt['end_time'] and end_datetime > appt['start_time']:
                print("There is a scheduling conflict. Please select a different time slot.")
                return
        
        self.appointment_diary.append({
            'start_time': start_datetime,
            'end_time': end_datetime,
            'purpose': purpose
        })
        print("Appointment scheduled successfully.")
    
    def cancel_appointment(self, date, start_time):
        start_datetime = datetime(date.year, date.month, date.day, start_time.hour, start_time.minutes)
        
        for appt in self.appointment_diary:
            if appt['start_time'] == start_datetime:
                self.appointment_diary.remove(appt)
                print("Appointment canceled successfully.")
                return
        
        print("Appointment not found.")
    
    def check_appointment(self, date, start_time, end_time):
        start_datetime = datetime(date.year, date.month, date.day, start_time.hour, start_time.minutes)
        end_datetime = datetime(date.year, date.month, date.day, end_time.hour, end_time.minutes)
        
        for appt in self.appointment_diary:
            if start_datetime < appt['end_time'] and end_datetime > appt['start_time']:
                return True
        
        return False
    
    def retrieve_appointment_purpose(self, date, start_time):
        start_datetime = datetime(date.year, date.month, date.day, start_time.hour, start_time.minutes)
        
        for appt in self.appointment_diary:
            if appt['start_time'] == start_datetime:
                return appt['purpose']
        
        return None
    
    # def reschedule_appointment(self, old_date, old_start_time, new_date, new_start_time):
    #     old_start_datetime = datetime(old_date.year, old_date.month, old_date.day, old_start_time.hour, old_start_time.minutes)
    #     new_start_datetime = datetime(new_date.year, new_date.month, new_date.day, new_start_time.hour, new_start_time.minutes)
    #     new_end_datetime = new_start_datetime + timedelta(minutes=(old_start_time - old_start_time.to_24_hour_format
