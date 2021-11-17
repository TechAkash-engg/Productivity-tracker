from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

#e = pd.read_csv("Contacts.csv")
e = pd.read_excel("weekly_mail.xlsx")
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login('akashrajpbhat@gmail.com','----')

body = ("""
This is your performance report
""")
subject = "employee report generator"
fromaddr='akashrajpbhat@gmail.com'

for index, row in e.iterrows():
    #print (row["Emails"]+row["PDF"])
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    filename = row["PDF"]
    toaddr = row["Emails"]
    attachment = open(row["PDF"], "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    

#print("Emails sent successfully")

server.quit()
