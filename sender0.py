# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "bobpaslabobine@gmail.com"
email_password = ...
def send(to:iter,title,mess):
    # create email
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = email_address
    msg['To'] = ",".join(to)
    msg.set_content(mess)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
if __name__=="__main__":
    send(["momoladebrouill@gmail.com"],"sex",open("content.txt").read())
            

