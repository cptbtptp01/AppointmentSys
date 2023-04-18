
# appt_Appointment.py
# huiru yang (yang.huir@northeastern.edu)
# April 17 2023

from appt_AppointmentDiary import AppointmentDiary

class User:
    """A class that represents a user in the appointment management system.
    Attributes:
        name (str): The name of the user.
        appointment_diary (AppointmentDiary()): The appointment diary of the user.
        all_users (dict): {"user1": User object,"user2": User object,"user3": User object, ...}
    """
    # class variable
    all_users = {}

    def __init__(self, name: str) -> None:
        """Initializes a new User instance.
        Args:
            name (str): The name of the user.
        """
        self.name = name
        self.appointment_diary = AppointmentDiary()
    
    def __str__(self):
        """Returns the string representation of the User.
        """
        return f"{self.name}"

    @classmethod
    def get_user(cls) -> 'User':
        """Class method that gets a User instance from user input.
        Returns:
            User instance: an existing user instance or a new user instance
        """
        while True:
            username = input("\nEnter your username (must be at least 2 characters): ")
            if len(username) < 2:
                # avoid empty/1-length input
                print("Username must be at least 2 characters long.")
            elif username.isdigit():
                print("Username cannot only contain numbers.")
            elif not any(c.isalpha() for c in username):
                print("Username must contain at least one letter and cannot only contain numbers.")
            elif not username.isalnum() and '-' not in username and '_' not in username:
                print("Username can only contain letters, numbers, hyphens, and underscores. Please try again.")
            else:
                break
        return cls.all_users.get(username, cls(username))

    @classmethod
    def sort_user(cls) -> dict:
        """Sort all_user dictionary
            Returns:
                dict
        """
        keys = list(cls.all_users.keys())
        keys.sort()
        cls.all_users = {i: cls.all_users[i]for i in keys}
        return cls.all_users

    @classmethod
    def add_user(cls) -> str:
        """Class method that adds a new User instance to the system.
        Returns:
            str: A message indicating whether the user was added or not.
        """
        new_user = cls.get_user() # a user object
        if new_user.name in cls.all_users:
            return f"Sorry, {new_user} already exists, please try again."
        else:
            cls.all_users[new_user.name] = new_user
            cls.sort_user()
            return f"Welcome, {new_user}! Your profile has been added."
    
    @classmethod
    def check_user(cls) -> 'User' or None:
        """Class method that checks if a User instance exists in the system.
        Returns:
            User or None: A User instance if it exists, None otherwise.
        """
        user = cls.get_user()
        if user.name in cls.all_users:
                return user
        return None
    
    @classmethod
    def delete_user(cls) -> str:
        """Class method that deletes a User instance from the system.
        Returns:
            str: A message indicating whether the user was deleted or not.
        """
        user = cls.get_user()
        if user.name in cls.all_users:
            del cls.all_users[user.name]
            cls.sort_user()
            return f"User {user} has been deleted."
        return f"User {user} not found."
        
    @classmethod
    def show_user(cls) -> str:
        """Class method that returns a string contains all usernames in the system.
        Returns:
            str: A string contains all usernames in the system.
        """
        if not cls.all_users:
            return "The system has 0 user."
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        users = [username for username in cls.all_users.keys()]
        return f"The system has {plural('users', len(cls.all_users))}:\n" + "\n".join(users)
    
    @classmethod
    def get_all(cls) -> str:
        """Class method that returns a string with information about all user in the system.
        Returns:
            str: A string with information about all user in the system.
        """
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        user_info = []
        # item() method returns key-value pairs -> (key, value) -> (username, user obj)
        # need to unwrap the tuple first
        for username, user in cls.all_users.items(): 
            user_str = f"{username}:"
            if user.appointment_diary.diary:
                for date, appts in user.appointment_diary.diary.items():
                    for appt in appts:
                        appt_str = f"{appt.start_time} - {appt.end_time}: {appt.purpose}"
                        user_str += f"\n{date}: {appt_str}"
                user_info.append(user_str)
            else:
                user_str += ' no appointment yet'
                user_info.append(user_str)
        return f"The system has {plural('users', len(cls.all_users))}.\n" + "\n".join(user_info)