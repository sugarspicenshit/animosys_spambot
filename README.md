# Animosys Spambot

A bot that snatches slots from cavemen who still use the website with mouse and keyboard.

This bot is a WIP.

(o btw my friend said this bot could take down servers. i mean hes not wrong if like 10 ppl use it on animosys lmfao)

## 📋 Prerequisites

Get these before using the script:

1. Selenium for Python
2. chromedriver.exe (for your current version of Chrome)
3. A MyLasalle account
4. A cart filled with subjects on your Animosys

## 🤔 How to use

After getting the prerequisite items, do these to run the bot:

1. Download all the files
2. Run animosys.py

## 🔐 Set your MLS Account credentials

Under default settings, the program will ask for your MLS username and password. This can be skipped by modifying the 
`account.ini` file.  

In the `account.ini` file, fill up the `username` and `password` keys with your MLS username and password.

> ⚠️ **WARNING** For security reasons, it is not recommended to do this. Your MLS username and password will be rendered vulnerable.  

> ❗️ **IMPORTANT** If [`QuickRunEnabled`](#quickrunenabled) is set to `False`, the program will still ask for your MLS username and password. To prevent this, change the value to `True`.

## ⚙️ Modify the spambot's settings

The spambot's settings can be changed by modifying the `settings.ini` file. Below are the following settings.

> ⚠️ **WARNING** Do NOT modify unless you know what you're doing.

### QuickRunEnabled

Before the spambot starts spamming the enlistment process, the bot will first do the following:
1. Prompt you to select the `chromedriver.exe` location
2. Ask for your MLS username and password
3. Add the subjects in the `Subjects` key to your cart

> ✅ To skip these, `QuickRunEnabled` must be set to `True`

### ChromedriverLocation

The location of the folder where your `chromedriver.exe` is stored.

> ❗️ **IMPORTANT** If [`QuickRunEnabled`](#quickrunenabled) is set to `False`, the program will still prompt for the Chromedriver location. To prevent this, change the value to `True`.

### Subjects

🚧 This feature is still a **WIP**

A list of subject codes you want the bot to add to your cart.  
Each subject code is separated with a __space__.  

>💡 By adding subjects, the [4th prerequisite](#-prerequisites) can be ignored.

> 📝 *Example*  
> Enlist for classes with subject codes: 8495, 283, 691, 4870   
> Change this line in the file: `Subjects = 8495 283 691 4870`

> ❗️ **IMPORTANT** If [`QuickRunEnabled`](#quickrunenabled) is set to `False`, the program will not add the subjects to your cart and skip straight to spamming enlistment requests. To prevent this, change the value to `True`.

### SleepTimer

A delay (in seconds) interval in between each request during the enlistment process.
