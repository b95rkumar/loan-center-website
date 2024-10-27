import smtplib

sender = "demo@demomailtrap.com"
receiver = "b95rkumar@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""
try:
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login("f2959531319015", "")
        server.sendmail(sender, receiver, message)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
    