#
#
#

"""
"""
class User:
    """...
    """
    # a class variable to store all the user name
    all_users = []

    def __init__(self, f_name:str, l_name:str) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.appointment_diary = []
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    @classmethod
    def add_user(cls) -> str:
        while True:
            username = input("Enter your Full Name:").split()
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
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        users = [str(user) for user in cls.all_users]
        return f"The system has {plural('users', len(cls.all_users))}.\n" + ",".join(users)

class Appointment:
    ...

class AppointmentDiary:
    ...



from datetime import datetime, timedelta

appointments = [(datetime(2012, 5, 22, 10), datetime(2012, 5, 22, 10, 30)),
                (datetime(2012, 5, 22, 12), datetime(2012, 5, 22, 13)),
                (datetime(2012, 5, 22, 15, 30), datetime(2012, 5, 22, 17, 10))]



if __name__ == "__main__":
    ...
