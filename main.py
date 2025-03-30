import imaplib, email, os, time, sys
import re


def login_to_gmail():
    password = "pbyu ylci ejks iqlr"
    username = "developers.alg9567@gmail.com"
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    
    # Login to the gmail account
    imap_server.login(username, password)
    return imap_server

def get_mails(imap):
    for resp in imap.list()[1]:
        cont = resp.decode().split(' "/" ')
        imap.select('INBOX')
        status, messages = imap.search(None, 'ALL')
        
        # loop through the messages
        for count in messages[0].split():
            _, msg = imap.fetch(count, "(RFC822)")
            message = email.message_from_bytes(msg[0][1])
            if message.is_multipart():
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        msg_content = part.get_payload(decode=True)
                        msg_body = msg_content.decode('utf-8')
                        break
                    else:
                        msg_content = message.get_payload(0).get_payload(decode=True)
                        msg_body = msg_content.decode('utf-8')
            else:
                msg_content = message.get_payload(decode=True)
                msg_body = msg_content.decode('utf-8')
            
        print(msg_body)
        break


def run():
    imap = login_to_gmail()
    get_mails(imap)

if __name__ == "__main__":
    run()