## animosys.py v1.1 ############################################################
##                                                                             #
## This script is a spam click bot that spams the animo.sys server with        #
## enrollment confirmation requests.                                           #
##                                                                             #
## Author: SugarSpiceNShit                                                     #
##                                                                             #
################################################################################

from selenium import webdriver
from time import sleep
from datetime import datetime
from msvcrt import kbhit
import console
from getpass import getpass
import traceback


## Script Settings #############################################################
##
## Variables that modify the script's behavior.
##
################################################################################

# Skips the process of setting up the script.
# RECOMMENDED: False
# Do not disable unless you know what you're doing.
quick_run_enabled = False

# Prompts the user for the file location of the chromdriver executable.
# RECOMMENDED: True
# Do not disable unless chromedriver_location is not empty.
get_chromedriver_location_enabled = True and not quick_run_enabled

# File location of the chromedriver.
# If this string is filled with a valid file location of the
# chromedriver executable, then get_chromedriver_location_enabled
# can be set to False.
chromedriver_location = ""

# Prompts the user for their MyLasalle credentials.
# RECOMMENDED: True
# Do not disable unless username and password are filled with
# valid credentials.
get_credentials_enabled = True and not quick_run_enabled

# MyLasalle credentials.
# It is recommended that these are left empty for
# security reasons.
# If filled with valid credentials, then get_credentials_enabled
# can be set to False.
username = ""
password = ""

# Asks the user for which subjects to enroll.
# Can be disabled if the user already has subjects in
# the cart.
# WARNING: This feature is a WIP and currently does nothing.
get_subjects_enabled = False and not quick_run_enabled

# Delay in between spam requests (in seconds).
sleep_timer = 0

################################################################################


## SCRIPT EXECUTION STARTS HERE ################################################

line = '\n'+'='*75+'\n'

console.log('Animosys Enlistment Clickbot now booting up...')
console.log('Written by: SugarSpiceNShit')

if get_chromedriver_location_enabled:
    print(line)
    print('Enter the file location of the chromedriver executable:')
    print(r'Example: C:\Users\myUser\chromedriver_folder')
    print()
    chromedriver_location = input('>> ') + r'\chromedriver.exe'
    print(line)

console.log('Now opening chromedriver executable located at ' + chromedriver_location)

if chromedriver_location:
    try:
        driver = webdriver.Chrome(chromedriver_location)
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
    else:
        console.success('Chrome successfully opened!')
        console.log('Now opening animo.sys.dlsu.edu.ph.')

try:
    driver.get('https://animo.sys.dlsu.edu.ph/psp/ps/?cmd=login')
except:
    console.error('Cannot open animo.sys.dlsu.edu.ph! Possible causes are website might be down; ' + 
        'errors in your internet connection; or address has been changed.')
    exit()
else:
    console.success('Website has been successfully opened!')
    console.log('Now logging in.')

while True:
    if get_credentials_enabled:
        print('Enter your username and password: ')

        username = input('Username: ')
        password = getpass('Password: ')

    username_input = '//*[@id="userid"]'
    driver.find_element_by_xpath(username_input).click()
    driver.find_element_by_xpath(username_input).send_keys(username)

    password_input = '//*[@id="pwd"]'
    driver.find_element_by_xpath(password_input).click()
    driver.find_element_by_xpath(password_input).send_keys(password)

    login_button = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[4]/td[3]/input'
    driver.find_element_by_xpath(login_button).click()

    if username_input:
        console.error('Login failed! Re-enter credentials.\n')

        if not get_credentials_enabled:
            exit()
    else:
        break

console.success('Login successful!')

if get_subjects_enabled:
    print('\nEnter all the subject codes.')
    print('\nEnter 0 once done.\n')

    while True:
        code = input("Subject Code: ")

        if int(input)==0: break

console.log('Now attempting to force enlistment!')
current_time = str(datetime.now().hour) + ':' + str(datetime.now().minute)
console.log('Current time is ' + datetime.strptime(current_time, "%H:%M").strftime('%I:%M %p'))

# xpath of all buttons clicked in this process
confirm_button = r'//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$114$"]'
finish_button = r'//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]'
add_another_class_button = r'//*[@id="DERIVED_REGFRM1_SSR_LINK_STARTOVER"]'

count = 0

while True:

    try:

        sleep(sleep_timer)

        # Opens the 'Add Classes' webpage.
        # Fixes the bug where the 'Proceed to Step 2 of 3' button could not be found.
        driver.get('https://animo.sys.dlsu.edu.ph/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGB&EMPLID=11846712&ENRL_REQUEST_ID=&INSTITUTION=DLSU&STRM=1203')

        if kbhit(): break

        console.log(f'Attempting to click button: \'Proceed to Step 2 of 3\'! [{count}]')

        driver.find_element_by_xpath(confirm_button).click()

        console.success(f'Clicking button: \'Proceed to Step 2 of 3\', successful! [{count}]')

        console.log(f'Attempting to click button: \'Finish Enrolling\'! [{count}]')

        # Fixes bug where webdriver can't find 'Finish Enrolling' button.
        driver.refresh()

        driver.find_element_by_xpath(finish_button).click()

        console.success(f'Clicking button: \'Finish Enrolling\', successful! [{count}]')

        console.success(f'Attempt {count} at forcing enlistment is successful!')

        count += 1
            
    except:
        console.warning(f'Failed to click button! Trying again...')

        
console.log('Script execution successful!\n')

driver.quit()