
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


# The line `html = Template(Path("test.html").read_text())` is reading the content of a file named
# "test.html" and storing it as a Template object in the variable `html`. This allows the content of
# the HTML file to be used as a template for email content, where placeholders can be substituted with
# actual values using the `substitute()` method.
html = Template(Path("test.html").read_text())
email = EmailMessage()
email['from'] = 'Herman Newman'
email['to'] = "ricchysore@gmail.com"
email['subject'] = 'Test-mail from richmondsogo with python'

# The line `email.set_content(html.substitute({"no": "full"}), "html")` is setting the content of the
# email message.
email.set_content(html.substitute({"no": "full"}), "html")



# The code block `with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:` is establishing a
# connection to the SMTP server of Gmail with the specified host and port.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # The code `smtp.login("richmondsogo@gmail.com", "nrfc jdyt syqr dfcs")` is authenticating the
    # user with the SMTP server by providing the email address "richmondsogo@gmail.com" and the
    # corresponding password "nrfc jdyt syqr dfcs". This step is necessary to establish a secure
    # connection and send emails through the SMTP server.
    smtp.login("richmondsogo@gmail.com", "nrfc jdyt syqr dfcs")
    smtp.send_message(email)
  # The line `print("all good boss")` is simply outputting the message "all good boss" to the console.
  # This message serves as a confirmation or indication that the email sending process has been
  # completed successfully up to that point. It's a way to inform the user or developer that the email
  # has been sent without any apparent issues.
    print("all good boss")
