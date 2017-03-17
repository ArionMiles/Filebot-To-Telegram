import requests
import sys
import json
import ConfigParser
import argparse

# Read settings from creds.ini
config = ConfigParser.RawConfigParser()
config.read('creds.ini')
API_KEY_TOKEN = config.get('CREDS', 'API_TOKEN')
CHAT_ID = config.get('CREDS', 'CHAT_ID')

parser = argparse.ArgumentParser(description="Filebot report tool.")
parser.add_argument('-title','-t', type=str, help="Message title", required=True)
parser.add_argument('-message','-m', type=str, help="Message content", required=False, default="")
args = parser.parse_args()

title = args.title
message = args.message

if args.message == "":
	message = title
else:
	message = title + "\n" + message

# defining the api-endpoint 
API_ENDPOINT = "https://api.telegram.org/bot" + API_KEY_TOKEN + "/sendMessage" 
 
# data to be sent to api
data = {'text':message,
        'chat_id':CHAT_ID,
        'parse_mode': 'markdown'}
 
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
status = str(r.status_code)
parsed_json = json.loads(r.text)
ok = str(parsed_json['ok'])
if "error_code" in parsed_json:
	error_code = str(parsed_json['error_code'])

# extracting response text 
if r.status_code == 200:
	print ("Message sent!")
else:
	print "OK: " + ok + "\n" + "Error: " + error_code + "\n" + "Description: " + parsed_json['description']