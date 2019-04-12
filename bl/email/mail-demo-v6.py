
import os
import smtplib
import imghdr


from email.message import EmialMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

EMAIL_PSWD =os.environ.get('EMAIL_PWD')

msg = EmailMessage()



contact = ['rj.rosag@gmail.com', 'g70375502@hotmail.com']
msg['Subject'] = 'Check out stitch as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contact 
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<doc HTML>
""", subtype = 'html')










	msg.add_attachment(file_data, maintype='application', subtype='octed-stream', filename="file_name")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:



	smpt.login(EMAIL_ADDRESS, EMAIL_PSWD)



















	smpt.send_message(msg)
