from tkinter import filedialog
import os


def get_chromedriver_location():
    """Chromedriver executable location prompt"""

    print('Select the chromedriver executable.')

    # Opens the File Selection window.
    chromedriver_location = filedialog.askopenfilename(title='Select chromedriver executable',
                                                       initialdir=os.getcwd())

    return chromedriver_location


def get_credentials():
    """MLS account username and password prompt"""

    # Hides the password as the user types it.
    try:
        # If the password field is blank during user prompt, then getch couldn't be imported.
        # As a result, the getpass module being used as a fallback.
        import getch

        def getpass(prompt):
            """Replacement for getpass.getpass() which prints asterisks for each character typed"""
            print(prompt, end='', flush=True)
            buf = ''
            while True:
                ch = getch.getch()
                if ch == '\n':
                    print('')
                    break
                else:
                    buf += ch
                    print('*', end='', flush=True)
            return buf
    except ImportError:
        from getpass import getpass

    print('Enter your username and password: ')
    username = input('Username: ')
    password = getpass('Password: ')

    return username, password
