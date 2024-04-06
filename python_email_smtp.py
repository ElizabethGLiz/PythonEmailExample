import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Connect to the SMTP server
smtp_server = 'smtp.example.com'
port = 587
server = smtplib.SMTP(smtp_server, port)
server.starttls()

# Login to the server
server.login('your_email@example.com', 'your_password')

# Create the email message
sender_email = 'your_email@example.com'
receiver_email = 'recipient@example.com'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Test Email'
body = 'This is a test email sent from Python.'
message.attach(MIMEText(body, 'plain'))

# Send the email
server.sendmail(sender_email, receiver_email, message.as_string())

# Close the connection to the SMTP server
server.quit()
