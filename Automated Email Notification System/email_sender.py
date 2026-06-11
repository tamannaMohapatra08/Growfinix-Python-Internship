import smtplib
from email.mime.text import MIMEText

sender_email = 
app_password = 

receiver_email = input("Enter receiver email: ")

msg = MIMEText("Hello! This is a test email sent using Python.")
msg["Subject"] = "Python Email Notification"
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)