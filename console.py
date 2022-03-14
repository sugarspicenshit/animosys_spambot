from datetime import datetime

class console:

    @staticmethod
    def log(event):
        """
        Prints out message in console to indicate script's current activity.
        """
        now = datetime.now()
        print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}] {event}')

    @staticmethod
    def warning(event):
        """
        Prints out warning message in console to indicate that the script
        could not be working as intended.
        """
        now = datetime.now()
        print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}] [WARNING] {event}')

    @staticmethod
    def error(event):
        """
        Prints out warning message in console to indicate that the script
        is not be working as intended and the execution flow is interrupted.
        """
        now = datetime.now()
        print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}] [WARNING] {event}')

    @staticmethod
    def success(event):
        """
        Prints out success message in console to indicate that the script
        worked as intended.
        """
        now = datetime.now()
        print(f'[{now.strftime("%Y-%m-%d %I:%M:%S %p")}] [SUCCESS] {event}')