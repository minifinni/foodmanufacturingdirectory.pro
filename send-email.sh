#!/bin/bash
# Email sender using Gmail SMTP
# Usage: ./send-email.sh "to@example.com" "Subject" "Body" ["cc@example.com"]

TO=$1
SUBJECT=$2
BODY=$3
CC=${4:-""}

GMAIL_USER="mini.finni.01@gmail.com"
GMAIL_PASS="ntolioepmpogllkv"
FROM_NAME="PickleGirlLDN"
FROM_EMAIL="mini.finni.01@gmail.com"

# Create MIME message
if [ -z "$CC" ]; then
    CC_HEADER=""
else
    CC_HEADER="Cc: $CC"
fi

MESSAGE="From: $FROM_NAME <$FROM_EMAIL>
To: $TO
$CC_HEADER
Subject: $SUBJECT
Content-Type: text/plain; charset=UTF-8

$BODY"

# Send via Gmail SMTP
echo "$MESSAGE" | curl -s --url 'smtps://smtp.gmail.com:465' \
    --ssl-reqd \
    --mail-from "$FROM_EMAIL" \
    --mail-rcpt "$TO" \
    --user "$GMAIL_USER:$GMAIL_PASS" \
    -T -

if [ $? -eq 0 ]; then
    echo "Email sent successfully to $TO"
else
    echo "Failed to send email"
    exit 1
fi
