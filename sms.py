import email, smtplib, ssl

def send_sms_via_email(
  number:str, 
  message:str, 
  sender_credentials:tuple, 
  subject:str="", 
  smtp_server="smtp.gmail.com", 
  smtp_port: int = 465):
  sender_email,email_password = sender_credentials
  my_provider = "txt.bell.ca"
  receiver_email = f"{number}@{my_provider}"
  email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

  with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
    email.login(sender_email,email_password)
    email.sendmail(sender_email,receiver_email,email_message)

