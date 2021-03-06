[![GitHub license](https://img.shields.io/badge/license-gpl-blue.svg)](https://raw.githubusercontent.com/fpacenza/web_scraper/main/LICENSE?token=AE7JDJALMZIYKRWFJPKRREDAGBLEQ)
<!-- [![GitHub release](https://img.shields.io/github/release/fpacenza/web_scraper.svg)](https://github.com/fpacenza/web_scraper/releases/latest) -->
<!-- [![GitHub issues](https://img.shields.io/github/issues/fpacenza/web_scraper.svg)](https://github.com/fpacenza/web_scraper/issues) -->

# A web scraper tool for finding product availability on the web

A useful tool to find availability of products on the web
# Release for win64 available
**Windows 64bit** - [Download](https://github.com/fpacenza/web_scraper/releases/download/v1.0.0/win64.zip)

# Set up
## Requirements
First of all, you need to install Python3. If you are on Linux or macOS you should not have any problem (python3, usually, is already installed). If you are runninf Windows, you need to manually install Python3.

### Install Python3 
- Windows
  - open a `powershell`
  - Type `python3` and press `enter`

- Linux
  - open a `terminal`
  - Type `sudo apt install python3` and press `enter`

- macOS
  - open a `console`
  - type `brew install python` and press `enter`


## Install the requirements
### Upgrade the pip3 module through python

- Windows
  - `python3 -m pip install --upgrade pip`
  - `pip3 install urllib3`
  - `pip3 install beautifulsoup4`

- Linux
  - `sudo python3 -m pip install --upgrade pip`
  - `sudo pip3 install urllib3`
  - `sudo pip3 install beautifulsoup4`

# Run the script
Before executing the script, check all the links that you find inside the file `ps5.py`. If they are not correct, please, update them.

Then, you can go in the `ps5_bot.py` file and update the `sender_email` and `receiver_email` with your `@gmail.com` accounts. Note that, the script will work only if you specify a gmail account and if you [allow less secure apps to access your SENDER gmail account](https://support.google.com/accounts/answer/6010255?hl=en). 

It is suggested to create an additional gmail account to be used as sender account.

## Execute the script
 - `python3 ps5_bot.py`
 - `Type your gmail sender account`
 - `Type the email address where you want to receive a notification`
 - `Type the password for your gmail sender account`
 - press `enter`

 Note that the password will be visible in your console but will be used a crypted `ssl` connection when the script will send the email, so the password **will be hidden** to the web. 
