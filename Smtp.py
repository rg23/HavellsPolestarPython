import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv


server = smtplib.SMTP('10.199.4.180',2521)

#server.starttls()

fromaddr = "MIS.havells@havells.com"

recipients = ['ravi.gupta@polestarllp.com']

#toaddr ="ravi.gupta@polestarllp.com"

msg = MIMEMultipart()

# cr = csv.reader(open("C:\\Users\\User\\Desktop\\BBND.csv","rb"))

#CR = open('C:\\Users\\User\\Desktop\\BBND.csv','r')
#reader = csv.reader(CR)

#s = CR.read() + '\n'

#print(repr(s))

body = '''<p>Hello,</p>
<br>
<p>Pls find attached the data using Python Framework.</P>
<P>
<br>
Regards,
<br>The fellowship maintainence <br>
<br></p>
'''

msg.attach(MIMEText(body, 'html'))
#msg.attach(MIMEText(s, 'html'))

msg['From'] = fromaddr
msg['To'] = ", ".join(recipients)
msg['Subject'] = "Early LUNCH"

print(body)

server.ehlo()
# server.starttls()
server.ehlo()
# server.login(fromaddr, "ravscricket")


#filename = "BBND.xlsx"
#attachment = open("""C:\\Users\\User\\Desktop\\BBND.xlsx""", "rb")

#part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

#msg.attach(part)

text = msg.as_string()

server.sendmail(fromaddr,recipients, text)

server.quit()

#The /n separates the message from the headers
#server.sendmail("ravi.gupta@polestarllp.com", "ravi.gupta@polestarllp.com", msg)
