import re
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SMTP_SERVER = environ.get("SMTP_SERVER")
FROM_EMAIL = environ.get("FROM_EMAIL")
EMAIL_SUBJECT = environ.get("EMAIL_SUBJECT")

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

EMAIL_TEMPLATE_PATH = "emailTemplate.html"
EMAIL_TABLE_STYLE = "<style> table, th, td { border: 1px solid black; border-collapse: collapse; \
                    text-align: center; padding: 10px; margin-left: auto; margin-right: auto;} </style>"
HTML_TABLE_STR = "<tr> <td>{number}</td> <td>{postedOn}</td> <td>{postType}</td> <td>{description}</td> <td>{link}</td> </tr>"

def generateEmailHtmlStrFromResults(result, subId, channelName):
    templateStr = open(EMAIL_TEMPLATE_PATH).read()
    tableRowStr = ""
    count = 1
    for i in result:
        postType = i['postingCategory']
        description = i['postInfo']['description']
        postedOn = i['postInfo']['createdOn']
        link = "-"
        tableRowStr += HTML_TABLE_STR.format(number = count, postedOn = postedOn, postType = postType, description = description, link = link)
        count += 1
    finalHtmlStr = templateStr.format(tableStyle = EMAIL_TABLE_STYLE, tableStr = tableRowStr, subId = subId, channelName = channelName)
    return finalHtmlStr

'''
Send email on CentOS using the "mail" command.
Example:
echo "<html> Hello </html>" | mail -s "$(echo -e "Release Status [Green]\nContent-Type: text/html")" rdalwadi@uci.edu
subprocess.run(["echo",htmlBody, "https://github.com/apache/asterixdb.git", "master"])
subprocess.Popen("cmd",shell=True)
'''
def sendEmail(htmlBody, toEmail):
    # Check if email matchs valid email regex
    if not EMAIL_REGEX.match(toEmail):
        return False
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = toEmail
    msg['Subject'] = EMAIL_SUBJECT

    msg.attach(MIMEText(htmlBody, 'html'))

    server = smtplib.SMTP(SMTP_SERVER)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, toEmail, text)
    server.quit()
    print("Sent notification email to", toEmail)
