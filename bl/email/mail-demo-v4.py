
import os
import smtplib
import imghdr


from email.message import EmialMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

EMAIL_PSWD =os.environ.get('EMAIL_PWD')

msg = EmailMessage()


msg['Subject'] = 'Check out stitch as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'rj.rosag@gmail.com'
msg.set_content('Image attached')

attachments = ['Resume.pdf']
for file in attachments:


	with open(attachments, 'rb') as f:

		file_data = f.read()
		file_type = imghd.what(f.name)


	msg.add_attachment(file_data, maintype='application', subtype='octed-stream', filename="file_name")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:



	smpt.login(EMAIL_ADDRESS, EMAIL_PSWD)



















	smpt.send_message(msg)
