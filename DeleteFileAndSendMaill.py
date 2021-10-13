
from os.path import isfile, join
import os
import glob
import smtplib, ssl

files = []
for file in glob.glob("C:/Users/Administrator/Documents/data/*.json"):
    files.append(file)


deleteFiles = []
for f in files:
    if not os.path.getsize(f):
        deleteFiles.append(f)
        os.remove(f)


if len(deleteFiles) > 0:

    sender_email = "seuemail@gmail.com"  
    receiver_email = "receiver_email@gmail.com"  
    password = "password"

    title = "Scrapy - Empty Files"
    message =  ""
    
    i = 1
    for s in deleteFiles:
        message = message + str(i) + " - " + s+ "\n"
        i+=1

    message = 'Subject: {}\n\n{}'.format(title.encode("UTF-8"), message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    