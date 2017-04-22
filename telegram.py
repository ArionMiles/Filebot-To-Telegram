'''Import requirements'''
import argparse
import json
import ConfigParser
import requests

# Read settings from creds.ini
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('creds.ini')
API_KEY_TOKEN = CONFIG.get('CREDS', 'API_TOKEN')
CHAT_ID = CONFIG.get('CREDS', 'CHAT_ID')

PARSER = argparse.ArgumentParser(description="Filebot report tool.")
PARSER.add_argument('-title', '-t', type=str, help="Message title", required=True)
PARSER.add_argument('-message', '-m', type=str, help="Message content", required=False, default="")
ARGS = PARSER.parse_args()

TITLE = ARGS.title
MESSAGE = ARGS.message

if ARGS.message == "":
    MESSAGE = TITLE
else:
    MESSAGE = TITLE + "\n" + MESSAGE

# Defining the api-endpoint
API_ENDPOINT = "https://api.telegram.org/bot" + API_KEY_TOKEN + "/sendMessage"

# Data to be sent to API
DATA = {'text':MESSAGE,
        'chat_id':CHAT_ID,
        'parse_mode': 'markdown'}

# sending post request and saving response as response object
R = requests.post(url=API_ENDPOINT, data=DATA)
STATUS = str(R.status_code)
DICT = json.loads(R.text)
OK = str(DICT['ok'])
if "error_code" in DICT:
    ERROR_CODE = str(DICT['error_code'])

# Extracting response text
if R.status_code == 200:
    print "Message sent!"
else:
    print "OK: " + OK + "\n" + "Error: " + ERROR_CODE + "\n" + "Description: " + DICT['description']
