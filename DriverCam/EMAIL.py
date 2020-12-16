
import smtplib   
# list of email_id to send the mail 
li = ["ayushwagdre0511@gmail.com"] 
  
for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session 
    s.starttls() # start TLS for security
    s.login("ayushwagdre05@gmail.com", "Mahendra051196")# Authentication 
    message = "Message_you_need_to_sendjiiiiiiiiiiii"
    s.sendmail("nancy12341510@gmail.com", dest, message) # sending the mail 
    s.quit()## terminating the session
