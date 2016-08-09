import smtplib


server=smtplib.SMTP('smtp.gmail.com',587)
#replace first argument with the server address and second one with port number 
server.starttls()
server.login('your email id','your password')
server.sendmail('your email id ','email id to which u want to send email','your message here')
#replace first argument with your email id second with the email to whichu want to send email and third with your message
