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
    options = {'a': User.add_user,'d': User.delete_user, 'l': User.show_user,'s': AppointmentDiary.schedule_appt,'c': AppointmentDiary.cancel_appt, 'f': AppointmentDiary.check_appt,'x': exit_program}
    print()
    # terminate only if user choose to exit
    while True:
        # print main menu
        print('Welcome to Appointment Management System! What would you like to do?\n'+'\n'+'[a] Add new user'+'\n'+'[d] Delete an existing user'+'\n'+'[l] List existing users'+'\n'+'[s] Schedule an appointment'+'\n'+'[c] Cancel an appointment'+'\n'+'[f] Check for appointment on certain date and time'+'\n'+'[p] Retrieve purpose of an appointment'+'\n'+'[r] Reschedule an existing appointment'+'\n'+'[x] Exit the system')
        try:
            # prompt user for choice
            choice = input('\nEnter Choice: ').lower()
            if choice in ['a', 'd', 'l', 'x']:
                print(options[choice](), '\n')
            elif choice == 's':
                user = User.check_user()
                if not user:
                    print("User not found.")
                    continue
                print(options[choice](user.appointment_diary))
                print(f"Here is your current diary:\n{user.appointment_diary}")
            elif choice == 'c':
                user = User.check_user()
                if not user:
                    print("User not found.")
                    continue
                print(options[choice](user.appointment_diary))
            elif choice == 'f':
                user = User.check_user()
                if not user:
                    print("User not found.")
                    continue
                print(options[choice](user.appointment_diary))
                
            else:
                print("placeholder")
        except ValueError:
            print('Please enter a/d/l/s/c/f/p/r/x.\n')