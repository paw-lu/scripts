import os
import smtplib
import ssl
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import schedule


def send_email(username, recipient, subject, body, attachment=None):
    """Send email via FRB Outlook

    :param username: Outlook username that is also used in the "From" field
        e.g. pyderpuffgirls@gmail.com
    :param recipient: a string or list of the email address of recipient(s)
    :param subject: the subject of email
    :param body: the body of email
    :param attachment: a string or list of the path(s) of the file(s) to attach, default: None

    Shamelessly copied from https://changhsinlee.com/pyderpuffgirls-ep4/
    """

    smtp_server = os.environ["SMPT_SERVER"]

    # https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
    if isinstance(recipient, str):
        recipient = [recipient]
    recipients_string = ", ".join(
        recipient
    )  # e.g. "person1@gmail.com, person2@gmail.com"

    # create email
    email = MIMEMultipart()

    # Add body, then set the email metadata
    if body is not None:
        content = MIMEText(body)
        email.attach(content)

    email["Subject"] = subject
    email["From"] = username
    email["To"] = recipients_string

    if attachment is not None:
        _add_attachments(email, attachment)

    with smtplib.SMTP(smtp_server) as conn:
        conn.sendmail(username, recipient, email.as_string())
        print(f"Sent email to {recipients_string}")

    pass


def _add_attachments(mime_part: MIMEMultipart, file_paths):
    """
    Add attachment to the email object from file paths
    """

    if isinstance(file_paths, str):
        file_paths = [file_paths]

    for file_path in file_paths:
        file_name = Path(file_path).name

        with open(file_path, "rb") as file:
            part = MIMEApplication(file.read())

        part.add_header("Content-Disposition", f"attachment; filename={file_name}")
        mime_part.attach(part)

    return mime_part


if __name__ == "__main__":
    outlook_username = os.environ["OUTLOOK_USERNAME"]
    schedule.every().day.at("23:00").do(
        send_email,
        username=outlook_username,
        recipient="pcosta@firstrepublic.com",
        subject="Yo check out this mountain",
        body="Mountain bigh",
        attachment="mountain.png",
    )

    while True:
        schedule.run_pending()
        time.sleep(1)
