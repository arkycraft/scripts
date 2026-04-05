import smtplib
def send_phishing_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()