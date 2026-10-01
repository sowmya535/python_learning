#simple mail message
import smtplib
sender = 'sowmyachebrolu55@gmail.com'
receiver = 'wd.rkad@gmail.com'
password = 'qkrjuwxjnobzhina'
message = 'hi'
with smtplib.SMTP('smtp.gmail.com', '587') as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.sendmail(sender,receiver,message)
print('Mail sent')


# to send files or any attachments
import smtplib
from email.message import EmailMessage
sender = 'sowmyachebrolu55@gmail.com'
receiver = 'sowmyachebrolu5@gmail.com'
password = 'qkrjuwxjnobzhina'
message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Test Email'
message.set_content('Hello, this is a test email sent using Python.')
filenames = ['students.txt', 'day15.py']
for filename in filenames:
    with open(filename, 'rb') as f:
        file = f.read()
        message.add_attachment(file, maintype = 'application', subtype = 'pdf' )

with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password)
    conn.send_message(message)

print('Mail sent successfully')






















































































































































































































































































