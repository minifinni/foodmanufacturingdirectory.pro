#!/usr/bin/env python3
"""
Email sender for manufacturer outreach
Uses Gmail SMTP to send emails from mini.finni.01@gmail.com
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
GMAIL_USER = "mini.finni.01@gmail.com"
GMAIL_PASS = "ntolioepmpogllkv"
FROM_NAME = "PickleGirlLDN"

def send_email(to_email, subject, body, cc_email=None):
    """Send email via Gmail SMTP"""
    
    msg = MIMEMultipart()
    msg['From'] = f"{FROM_NAME} <{GMAIL_USER}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    if cc_email:
        msg['Cc'] = cc_email
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        
        recipients = [to_email]
        if cc_email:
            recipients.append(cc_email)
        
        server.send_message(msg)
        server.quit()
        
        print(f"✓ Email sent successfully to {to_email}")
        if cc_email:
            print(f"  CC'd to {cc_email}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send email: {e}")
        return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 send_email.py <to> <subject> <body_file> [cc]")
        print("Example: python3 send_email.py contact@pickleco.com 'Inquiry' email.txt finn@email.com")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    cc_email = sys.argv[4] if len(sys.argv) > 4 else None
    
    with open(body_file, 'r') as f:
        body = f.read()
    
    send_email(to_email, subject, body, cc_email)

if __name__ == "__main__":
    main()
