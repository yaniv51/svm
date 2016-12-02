import httplib2
import os
import base64

from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = os.path.join(os.getcwd(), 'client_id.json')
APPLICATION_NAME = 'newSVM'
USER_ID = "me"


# A function that sends the email of the result to hadas.c@velismedia.com.
def send_email(message_text):
    credentials = get_credentials()

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    new_message = create_message(message_text)
    return send_message(USER_ID, new_message, service)


def send_message(user_id, message, service):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        return 'Message Id: %s' % message['id']
    except HttpError, error:
        return 'An error occurred: ' + error


def create_message(message_text):
    # to = 'hadas.c@velismedia.com'
    to = 'yaniv.israel@gmail.com'
    sender = '51.yaniv51@gmail.com'
    subject = 'Finished The Program'

    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message['body'] = message_text
    return {'raw': base64.urlsafe_b64encode(message.as_string())}


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'client_id.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
