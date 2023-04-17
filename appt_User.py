
from appt_AppointmentDiary import AppointmentDiary

class User:
    """A class that represents a user in the appointment management system.
    Attributes:
        name (str): The name of the user.
        appointment_diary (AppointmentDiary()): The appointment diary of the user.
        all_users (list): A list of all the users in the system.
    """
    # class variable
    all_users = []

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
            User: A User instance created from user input.
        """
        while True:
            username = input("Enter your username (must be at least 2 characters): ")
            if len(username) < 2:
                # avoid empty/1-length input
                print("Username must be at least 2 characters long.\n")
            elif username.isdigit():
                print("Username cannot only contain numbers.\n")
            elif not any(c.isalpha() for c in username):
                print("Username must contain at least one letter and cannot only contain numbers.\n")
            elif not username.isalnum() and '-' not in username and '_' not in username:
                print("Username can only contain letters, numbers, hyphens, and underscores. Please try again.\n")
            else:
                break
        return cls(username)

    @classmethod
    def add_user(cls) -> str:
        """Class method that adds a new User instance to the system.
        Returns:
            str: A message indicating whether the user was added or not.
        """
        new = cls.get_user()
        # check if user exists
        for user in cls.all_users:
            if user.name == new.name:
                return f"Sorry, {user} already exists, please try again."
        # add new user
        cls.all_users.append(new)
        return f"Welcome, {new}! Your profile has been added."
    
    @classmethod
    def check_user(cls) -> 'User' or None:
        """Class method that checks if a User instance exists in the system.
        Returns:
            User or None: A User instance if it exists, None otherwise.
        """
        to_check = cls.get_user()
        for user in cls.all_users:
            if user.name == to_check.name:
                return user
        return None
    
    @classmethod
    def delete_user(cls) -> str:
        """Class method that deletes a User instance from the system.
        Returns:
            str: A message indicating whether the user was deleted or not.
        """
        delete = cls.get_user()
        for user in cls.all_users:
            if user.name == delete.name:
                cls.all_users.remove(user)
                return f"User {delete} has been deleted."
        return f"User {delete} not found."
        
    @classmethod
    def show_user(cls) -> str:
        """Class method that returns a string contains all usernames in the system.
        Returns:
            str: A string contains all usernames in the system.
        """
        if not cls.all_users:
            return "The system has 0 user."
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        users = [str(user) for user in cls.all_users if user.appointment_diary.diary]
        users_empty = [str(user) for user in cls.all_users if not user.appointment_diary.diary]
        return f"The system has {plural('users', len(users))} holding appointments.\n" + "\n".join(users) + f"\nThe system has {plural('users', len(users_empty))} not holding appointments.\n" + "\n".join(users_empty)
    
    @classmethod
    def get_all(cls) -> str:
        """Class method that returns a string with information about all user in the system.
        Returns:
            str: A string with information about all user in the system.
        """
        plural = lambda word, n: f"{n} {word}" if n > 1 else f"{n} {word[:-1]}"
        user_info = []
        for user in cls.all_users:
            user_str = f"{str(user)}:"
            if user.appointment_diary.diary:
                for date, appts in user.appointment_diary.diary.items():
                    for appt in appts:
                        appt_str = f"{appt.start_time} - {appt.end_time}: {appt.purpose}"
                        user_str += f"\n{date}: {appt_str}"
                user_info.append(user_str)
            else:
                user_str += ' no appointment'
                user_info.append(user_str)
        return f"The system has {plural('users', len(cls.all_users))}.\n" + "\n".join(user_info)