import smtplib,ssl

port = 1025  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "bobpaslabobine@gmail.com"
receiver_email = "momoladebrouill@gmail.com"
password = ...
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

