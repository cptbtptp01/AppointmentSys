# main.py
# huiru yang (yang.huir@northeastern.edu)
# April 13 2023

"""
"""
# from datetime_appointment import User, Appointment, AppointmentDiary
# from user_appointment import Date, Time

from user_appointment import User, Appointment, AppointmentDiary
import string

def exit_program():
    print('Goodbye!\n')
    exit()

if __name__ == '__main__':
    # map the user's choice to the appropriate method
    options = {'a': User.add_user,'d': User.delete_user, 'l': User.show_user, 's': lambda: Appointment.schedule_appointment(None),'x': exit_program}
    print()
    # terminate only if user choose to exit
    while True:
        # print main menu
        print('Welcome to Appointment Management System! What would you like to do?\n'+'\n'+'[a] Add new user'+'\n'+'[d] Delete an existing user'+'\n'+'[l] List existing users'+'\n'+'[s] Schedule an appointment'+'\n'+'[c] Cancel an appointment'+'\n'+'[f] Check for appointment on certain date and time'+'\n'+'[p] Retrieve purpose of an appointment'+'\n'+'[r] Reschedule an existing appointment'+'\n'+'[x] Exit the system')
        # prompt user for choice
        choice = input('\nEnter Choice: ').lower()
        try:
            print(options[choice](), '\n')
        except KeyError:
            print('Please enter a/d/l/s/c/f/p/r/x.\n')