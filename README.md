# AirBnBAlertNewListing
Allow you to receive an alert (e-mail) when a new Listing is added on Airbnb, following your criterias.

## Airbnb Research
To make it works, you need to make first a research in the Airbnb Website following this requirements :
- Airbnb has to be in english
- You need to logout. The research has to be done wihtout being login in.
- Then, you can make you research and set your criterias (dates, price, place, etc). The script is currently only tested with Stays (not with Experiences and Restaurants). You can try Experiences and Restaurants but there is no garantee it will work.
- Once you are in the page in which you can show the map, you are good. You can update your filters here if needed. My advice is to use the option "show map" and to position yourself exactly in the area you want the alert to be active. The script will then check the listing only for what is available in the sized map.
- Finally, copy the url of the AIRBNB'page your are currently using. Airbnb update this url for every changes you make in the page (filter, map, etc). You will have to past it in the config file.

## Setup

- Clone the repo
- Create and complete a config.json file based on the example.config.json. Here are the different option you must set :
  - airBnbUrl : The url of your AIRBNB research (how to obtain it is described in the "Airbnb Research" section)
  - action : Time (in seconds) between each checks
  - mail : The mail who will receive the alert
  - mailSender : The mail you will use to send the alert
  - PasswordSender : Password of the mail you will use to send the alert
  - mailSMTP : SMTP of the mail you will use to send the alert
- Then, if you are using Docker :
  - docker build -t airbnbListing .
  - docker run -d airbnbListing
- If not :
  - You need to install Python 3.8
  - `pip install -r requirements.txt`
  - `python listing.py`
  - If the script has been properly configured and is working, you will receive an initialisation mail. If you don't, check the config file, something isn't working.
