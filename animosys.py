# animosys.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from msvcrt import kbhit
from console import console
import traceback
import tkinter
from tkinter import filedialog
import os
import configparser


def get_chromedriver_location():
    """Chromedriver executable location prompt"""
    print('Select the chromedriver executable.')

    # Opens the File Selection window.
    root = tkinter.Tk()
    root.withdraw()
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


# Read the 'settings.ini' file
config = configparser.ConfigParser()
config.read('settings.ini')

# Read the 'account.ini' file
account = configparser.ConfigParser()
account.read('account.ini')

# Parse the config file values to Python variables
quick_run_enabled = True if config['Main']['QuickRunEnabled'] == "True" else False
save_chromedriver_location = True if config['Advanced']['SaveChromedriverLocation'] == "True" else False
is_queue_present = True if config['Advanced']['IsQueuePresent'] == "True" else False

try:
    sleep_timer = float(config['Main']['SleepTimer'])
except:
    sleep_timer = 0

get_credentials_enabled = account['Account']['Username'] and account['Account']['Password']


# Script execution starts here
console.log('Animosys Enlistment Clickbot now booting up...')
console.log('Written by: SugarSpiceNShit')

# Prompt the user for the Chromedriver executable, if if it is not given in 'settings.ini'
# and 'quick_run_enabled' is disabled.
if not config['Main']['ChromedriverLocation'] and not quick_run_enabled:
    chromedriver_location = get_chromedriver_location()

    # Save the Chromedriver location in 'settings.ini' if SaveChromedriverLocation is enabled.
    if save_chromedriver_location:
        config['Main']['ChromedriverLocation'] = chromedriver_location

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
else:
    chromedriver_location = config['Main']['ChromedriverLocation'] + \
        r'\chromedriver.exe'

# Initialize Chromedriver
console.log(f'Opening chromedriver at {chromedriver_location}')
try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        options=options, executable_path=chromedriver_location)
    driver.minimize_window()
except:
    console.error('Cannot open chromedriver! Now printing traceback.')
    print()
    traceback.print_exc()
    print('Possible fixes:')
    print('1. Make sure your chromedriver is compatible with your current browser\'s version.')
    print('2. Make sure the full directory of your chromedriver executable is correct.')
    print('\nPress any key to continue...')
    while not kbhit():
        pass
    exit()

console.success('Chrome successfully opened!')
console.log('Now opening animo.sys.dlsu.edu.ph.')

# Open the Animo.sys website
driver.get('https://animo.sys.dlsu.edu.ph/psp/ps/?cmd=login')

console.success('Website has been successfully opened!')
console.log('Now logging in.')

# Log in to the Animo.sys website
while True:
    if not get_credentials_enabled or not quick_run_enabled:
        username, password = get_credentials()

    # Circumvents the virtual queue
    while True:
        try:
            username_input = '//*[@id="userid"]'
            driver.find_element(by=By.XPATH, value=username_input).click()
            driver.find_element(
                by=By.XPATH, value=username_input).send_keys(username)
        except:
            pass
        else:
            break

    password_input = '//*[@id="pwd"]'
    driver.find_element(by=By.XPATH, value=password_input).click()
    driver.find_element(by=By.XPATH, value=password_input).send_keys(password)

    login_button = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[4]/td[3]/input'
    driver.find_element(by=By.XPATH, value=login_button).click()

    sleep(5)

    try:
        driver.find_element(by=By.XPATH, value=username_input).click()
    except:
        break
    else:
        console.error('Login failed! Re-enter credentials.\n')
        if not get_credentials_enabled:
            console.error(
                'Requesting user for credentials is disabled. Now exiting the program.')
            while not kbhit():
                pass
            exit()

console.success('Login successful!')

# Flush the username and password variables after logging in
username = None
password = None

# Fill cart with subjects (if Subjects is not empty and has valid inputs)
# WARNING: Feature isn't currently working. Remove False to enable this feature.
if len(config['Main']['Subjects']) > 0 and not quick_run_enabled or False:
    class_number_field = r'//*[@id="DERIVED_REGFRM1_CLASS_NBR"]'
    class_number_enter_btn = r'//*[@id="DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$70$"]'
    next_btn = r'/html/body/form/div[1]/table/tbody/tr/td/div/table/tbody/tr[10]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[3]/div/span/a'

    subjects = config['Main']['Subjects'].split()

    for subject in subjects:
        driver.get(
            'https://animo.sys.dlsu.edu.ph/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL')

        try:
            console.log(f'Now adding subject {subject} to cart.')

            driver.find_element(by=By.XPATH, value=class_number_field).click()
            driver.find_element(
                by=By.XPATH, value=class_number_field).send_keys(subject)
            driver.find_element(
                by=By.XPATH, value=class_number_enter_btn).click()

            driver.find_element(by=By.XPATH, value=next_btn)
        except NoSuchElementException:
            console.log(
                f'Can\'t add subject {subject} to cart! Skipping to next subject')

console.log('Now attempting to force enlistment!')
current_time = str(datetime.now().hour) + ':' + str(datetime.now().minute)
console.log('Current time is ' +
            datetime.strptime(current_time, "%H:%M").strftime('%I:%M %p'))

confirm_button = r'//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$114$"]'
finish_button = r'//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]'
add_another_class_button = r'//*[@id="DERIVED_REGFRM1_SSR_LINK_STARTOVER"]'

count = 0

# Opens the 'Add Classes' webpage.
# Fixes the bug where the 'Proceed to Step 2 of 3' button could not be found.
driver.get('https://animo.sys.dlsu.edu.ph/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGB&EMPLID=11846712&ENRL_REQUEST_ID=&INSTITUTION=DLSU&STRM=1203')

# Start spam clicking the buttons
try:
    while True:
        try:
            console.log(
                f'Attempting to click button: \'Proceed to Step 2 of 3\'! [{count}]')

            while True:
                try:
                    confirm_button = driver.find_element(
                        by=By.XPATH, value=confirm_button)
                except:
                    pass
                else:
                    break

            confirm_button.click()

            console.success(
                f'Clicking button: \'Proceed to Step 2 of 3\', successful! [{count}]')
            
            sleep(sleep_timer)

            console.log(
                f'Attempting to click button: \'Finish Enrolling\'! [{count}]')

            # Fixes bug where webdriver can't find 'Finish Enrolling' button.
            driver.refresh()

            driver.find_element(by=By.XPATH, value=finish_button).click()

            console.success(
                f'Clicking button: \'Finish Enrolling\', successful! [{count}]')

            console.success(
                f'Attempt {count} at forcing enlistment is successful!')

            count += 1

        except:
            console.warning(f'Failed to click button! Trying again...')
except KeyboardInterrupt:
    console.log('Script execution successful!\n')
finally:
    driver.quit()
