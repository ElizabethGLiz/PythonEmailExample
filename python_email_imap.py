import imaplib

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL('imap.example.com')

# Login to the server
mail.login('your_email@example.com', 'your_password')

# Select the mailbox (inbox in this case)
mail.select('inbox')

# Search for emails
status, data = mail.search(None, 'ALL')

# Get the list of email IDs
email_ids = data[0].split()

# Loop through the email IDs and fetch the email data
for email_id in email_ids:
    status, data = mail.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]
    print(raw_email)


