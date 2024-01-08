import smtplib
# creates SMTP session
def sendNotificationToUser():
 s = smtplib.SMTP('smtp.gmail.com', 587)
 # start TLS for security
 s.starttls()
 # Authentication
 s.login("test@gmail.com", "sender_email_id_password")
 # message to be sent
 message = "Message_you_need_to_send"
 # sending the mail
 s.sendmail("testadmin@gmail.com", "testuser@gmail.com", message)
 # terminating the session
 s.quit()

