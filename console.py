from datetime import datetime


def log(event):
    """
    Prints out a message in console to indicate 
    the program's current activity.
    """
    now = datetime.now()
    print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}] {event}')


def warning(event):
    """
    Prints out a warning message in console to indicate 
    that the program might encounter an error.
    """
    now = datetime.now()
    print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}][WARNING] {event}')


def success(event):
    """
    Prints out success message in console to indicate 
    that the action worked as intended.
    """
    now = datetime.now()
    print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}][SUCCESS] {event}')


def error(event):
    """
    Prints out an error message in console to indicate
    that the program encountered an error during runtime.
    """
    now = datetime.now()
    print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}][ERROR] {event}')        