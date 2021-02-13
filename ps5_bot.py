from ps5 import check_ps5
import re
import os
import smtplib

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sender_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: PlayStation 5 Availability

PlayStation 5 IS NOW AVAILABLE"""


while 1:
    ps5_results = check_ps5(True)
    for result in ps5_results:
        if "disponibile" == str(result[1]).lower():
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                print(result[2])
                server.login(sender_email, password)
                message = """\
Subject: PlayStation 5 Availability

""" + str(result[2])
                server.sendmail(sender_email, receiver_email, message)


    ps5_results.clear()
