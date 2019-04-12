
import os
import smtplib



EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

EMAIL_PSWD =os.environ.get('EMAIL_PWD')



with smtplib.SMTP('localhost',1025 ) as smtp:





	subject = 'Grab diner this weeken?'
	body = 'How about dinner at 6pm this Saturday?'
	msg = f'Subject: {subject}\n\n{body}'

	SENDER = EMAIL_ADDRESS


	RECEIVER =  'rj.rosag@gmail.com'









	smpt.sendmail(SENDER, RECEIBER, msg)
