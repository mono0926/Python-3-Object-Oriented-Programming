import smtplib 
from email.mime.text import MIMEText
from collections import defaultdict

def send_email(subject, message, from_addr, *to_addrs,
        host="localhost", port=1025, headers):

    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

class MailingList:
    '''Manage groups of e-mail addresses for sending e-mails.'''
    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        return {e for (e, g) in self.email_map.items()
                if g & groups}

    def send_mailing(self, subject, message, from_addr,
            *groups, **kwargs):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr,
                *emails, **kwargs)
