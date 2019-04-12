
import os
import smtplib
from email.message import EmialMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

EMAIL_PSWD =os.environ.get('EMAIL_PWD')

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'rj.rosag@gmail.com'
msg.set_content('How about dinner at 6pm this Saturday?')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:



	smpt.login(EMAIL_ADDRESS, EMAIL_PSWD)



















	smpt.send_message(msg)
