# main.py
# huiru yang (yang.huir@northeastern.edu)
# April 13 2023

"""
"""
from appt_User import User
from appt_AppointmentDiary import AppointmentDiary

def exit_program():
    print('Goodbye!\n')
    exit()

if __name__ == '__main__':
    # map the user's choice to the appropriate method
    options = {'a': User.add_user,'d': User.delete_user, 'l': User.show_user,'s': AppointmentDiary.schedule_appt,'c': AppointmentDiary.cancel_appt, 'f': AppointmentDiary.check_appt,'p': AppointmentDiary.get_appt,'r':AppointmentDiary.reschedule_appt,'x': exit_program}
    # terminate only if user choose to exit
    while True:
        # print main menu
        print('-'*100)
        print('Welcome to Appointment Management System! What would you like to do?\n'+'\n'+'[a] Add new user'+'\n'+'[d] Delete an existing user'+'\n'+'[l] List existing users'+'\n'+'[s] Schedule an appointment'+'\n'+'[c] Cancel an appointment'+'\n'+'[f] Check for appointment on certain date and time'+'\n'+'[p] Retrieve purpose of an appointment'+'\n'+'[r] Reschedule an existing appointment'+'\n'+'[x] Exit the system')
        try:
            # prompt user for choice
            choice = input('\nEnter Choice(case not sensitive): ').lower()
            if choice in ['a', 'd', 'l', 'x']:
                print(options[choice](), '\n')
            elif choice in ['s', 'c', 'f', 'p', 'r']:
                user = User.check_user()
                if not user:
                    print("User not found.")
                    continue
                print(options[choice](user.appointment_diary))
            elif choice == 'admin':
                print(User.get_all())
            else:
                print('Please enter a/d/l/s/c/f/p/r/x.\n')
        except ValueError:
            print('Please enter a/d/l/s/c/f/p/r/x.\n')