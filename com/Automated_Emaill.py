import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('popoolatunde52@gmail.com', '08138579886')
server.sendmail('popoolatunde52@gmail.com', 'poptuma52@yahoo.com',
                "testing my email bot code and how to automated the sending")
