import smtplib
import schedule
import time

#sender email id and password

email_id = "your email id"
password = "your password"
    
    
server = smtplib.SMTP('smtp.gmail.com', 587) # 587 is default port number
server.ehlo()
server.starttls()
server.login(email_id, password)
    
to = input("Enter the email id:")    
message =input("Enter the message:")
    
server.sendmail(email_id,to,message)

print("Email has been sent")
    
server.close()
