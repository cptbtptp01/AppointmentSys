# main.py
# huiru yang (yang.huir@northeastern.edu)
# April 13 2023

"""
This is the main module of an Appointment Management System. It provides an interactive command-line interface for managing users and their appointments.

The system allows the user:
    -Add new user
    -Delete an existing user
    -List existing users
    -Schedule an appointment
    -Cancel an appointment
    -reschedule
    -Check for appointment on certain date and time
    -Retrieve purpose of an appointment

Please note:
    The system stores user data and appointment information in memory, and does not persist it across sessions.
"""

from classes.appt_User import User
from classes.appt_AppointmentDiary import AppointmentDiary

def exit_program():
    print('\nGoodbye!\n')
    exit()

if __name__ == '__main__':
    # map the user's choice to the appropriate method
    options = {'a': User.add_user,'d': User.delete_user, 'l': User.show_user,'s': AppointmentDiary.schedule_appt,'c': AppointmentDiary.cancel_appt, 'f': AppointmentDiary.check_appt,'p': AppointmentDiary.get_appt,'r':AppointmentDiary.reschedule_appt,'x': exit_program}
    # terminate only if user choose to exit
    while True:
        # print main menu
        print('\n'+'-'*100)
        print('Welcome to Appointment Management System! What would you like to do?\n'+'\n'+'[a] Add new user'+'\n'+'[d] Delete an existing user'+'\n'+'[l] List existing users'+'\n'+'[s] Schedule an appointment'+'\n'+'[c] Cancel an appointment'+'\n'+'[f] Check for appointment on certain date and time'+'\n'+'[p] Retrieve purpose of an appointment'+'\n'+'[r] Reschedule an existing appointment'+'\n'+'[x] Exit the system')
        try:
            # prompt user for choice
            choice = input('\nEnter Choice(case not sensitive): ').lower()
            if choice in ['a', 'd', 'l', 'x']:
                print('\n',options[choice]())
            elif choice in ['s', 'c', 'f', 'p', 'r']:
                user = User.check_user()
                if not user:
                    print("User not found.")
                    continue
                print(options[choice](user.appointment_diary))
            elif choice == 'admin': # for checking purpose
                print(User.get_all())
            else:
                print('Please enter a/d/l/s/c/f/p/r/x.')
        except ValueError:
            print('Please enter a/d/l/s/c/f/p/r/x.')