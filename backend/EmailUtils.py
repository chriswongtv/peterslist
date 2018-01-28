import subprocess

EMAIL_TEMPLATE_PATH = "emailTemplate.html"

HTML_TABLE_STR = "<tr> <td>{number}</td> <td>{type}</td> <td>{description}</td> <td>{link}</td> </tr>"

def generateEmailHtmlStr():
    templateStr = open(EMAIL_TEMPLATE_PATH).read()
    tableRowStr = ""
    for i in range(9):#result:
        tableRowStr += HTML_TABLE_STR.format(number = i, type = "Jobs",
                                                description = "Need Software Engineer", link = "Link")
    finalHtmlStr = templateStr.format(tableRowStr)
    print(finalHtmlStr)
    return finalHtmlStr

generateEmailHtmlStr()

'''
Send email on CentOS using the "mail" command.
Example:
echo "<html> Hello </html>" | mail -s "$(echo -e "Release Status [Green]\nContent-Type: text/html")" rdalwadi@uci.edu
'''
def sendEmail(htmlBody, subject, toEmail):
    return
    #subprocess.run(["echo",htmlBody, "https://github.com/apache/asterixdb.git", "master"])
    #subprocess.Popen("cmd",shell=True)
