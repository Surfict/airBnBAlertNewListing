# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
import smtplib
import requests
import re
import json


def sendmail(message):

    server = smtplib.SMTP_SSL(mailSMTP)
    server.connect(mailSMTP)
    server.ehlo()
    server.login(mailSender, PasswordSender)
    sender = mailSender
    receivers = [mail]

    try:
        server.sendmail(sender, receivers, message.encode('utf-8'))
    except smtplib.SMTPException as e:
        print(e)

    server.quit()
    print("Successfully sent email")



def parshtml():

    # Request to AirbnbPage
    req = requests.get(airBnbUrl)
    # Regex to find the listing number in the source code
    m = re.search('(?<="listings_count":)\d+', req.text)
    if m:
        found = m.group(0)
        print(found)

    global nbListing

    # When the script is called for the first time, we send an initialisation mail
    if (nbListing == -1):
        message = """
This is the initializaion mail\n
If you receive it, it means all is working fine.
Currently, """ + m.group(0) +  """ hosts are listed on Airbnb following your criterias.\n """ + airBnbUrl
        sendmail(message)
    else:
        if (m.group(0) > nbListing):
            message = """
A new listing on Airbnb has been detected.
Currently, """ + m.group(0) + """ hosts are listed on Airbnb following your criterias.\n """ + airBnbUrl
            sendmail(message)

    nbListing = m.group(0)


nbListing = -1

#Config
with open('./config.json', encoding='utf-8') as fichier:
    config = json.load(fichier)

#----------------------------------------------------------------------------Parameters-----------------------------------------------------------------------------------------------
mail = config['mail'] # This mail will receive the alert
mailSender = config['mailSender'] # This mail will send the alert
PasswordSender = config['PasswordSender']
mailSMTP = config['mailSMTP']
airBnbUrl = config['airBnbUrl']
action = config['action'] # Time between each check
#----------------------------------------------------------------------------End Parameters-------------------------------------------------------------------------------------------


while 1:
    parshtml()
    time.sleep(action)