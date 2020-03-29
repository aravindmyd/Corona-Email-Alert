from datetime import datetime


def create_mail(table_data, changed_message,namelist,email_list):
    

    for item in range(len(email_list)):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "aravindnaveenbot@gmail.com"
        receiver_email = email_list[item]
        password = "testpassword143"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Corona database Alert!"
        message["From"] = sender_email
        message["To"] = receiver_email

        msg = ""
        for i in changed_message:
            msg += i
            msg += "\n"
        text = f"""\
        Hey {namelist[item]},
        These are the changes in the corono count.
        {msg}.
        The  updated total list:
        """
        html = f"""\
        <html>
          <body>
            <h3>Hey {namelist[item]},</h3><br>
            <h3>zthese are the changes in the corona count.</h3><br>
            <h2>{msg}</h2><br>
            <h3>The  updated total list:</h3>
            {table_data}
          </body><br >
        <b>Sent by python Script</b>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print(f"Mail succesfully sent to {email_list[item]} on {str(datetime.now())}")


def first_mail(table_data,email,name):

        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "aravindnaveengames@gmail.com"
        receiver_email = email
        password = "testpassword143"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Corona database Alert!"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"""\
        Hey {name},
        This is your first update!

        The  updated total list:
        """
        html = f"""\
        <html>
          <body>
            <h2>Hey {name},</h2><br>
            <h3>This is your first update!</h3><br>
            <h3>We will keep you updated, whenever there is a update in Corona count!</h3>
            <h3>The  updated Corona list:</h3>
            {table_data}
          </body><br><br><br><br>
        <b><i>Sent by python Script</i></b>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print(f"Mail succesfully sent to {email} on {str(datetime.now())}")

