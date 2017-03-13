import requests
import sys
import json
if len(sys.argv) <3:
	print("Usage: telegram.py \"YOUR_MESSAGE\" \" Second_line \"")
else:
	message = sys.argv[1] + "\n" + sys.argv[2]
 
# Your API key & CHAT_ID here
API_KEY_TOKEN = "317819012:AAHE55sERM1t7bPPvUq8Y9HRU3Rm0T3omX0"
CHAT_ID = "317392351"

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