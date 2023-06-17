from smtplib import SMTP
from smtpd import DebuggingServer

smtp = SMTP()

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
SMTP_TIMEOUT = 10

smtp.set_debuglevel(True)
smtp.connect(SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT)
smtp.ehlo()

message = 'Poruka poslana iz pythona!'
sender = 'rterze1993@gmail.com'
recipient = 'anteprojic@gmail.com'

try:
    smtp.sendmail(sender, recipient, message)
except:
    print('Error while sending..')

smtp.quit()