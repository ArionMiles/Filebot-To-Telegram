# Telegram Bot for File Bot
Author: Arion_Miles

# Introduction
The bot is used in conjunction with a Automated Media Center, for example, my own setup consisting of Filebot (AMC Script), qBittorrent, and RSS Feeds to automatically send reports via push notifications on what content has been downloaded on to my Media Center, to my Phone.


# Motivation
By default, Filebot's AMC script provides a Pushbullet feature which sends a pushbullet notifications with a HTML documents of the files processed, and the title of the Pushbullet is the torrent's name. I needed something more concise, and the amount of text that can fit into a push notification and not require me to see the HTML doc along with it to see the files processed.

# Installation
We're using a telegram BOT for sending messages. [Start here](https://core.telegram.org/bots#3-how-do-i-create-a-bot) to learn how to create one for bot token. You can message [@get_id](https://telegram.me/get_id_bot) with `/my_id` and it'll give you a 9-digit Chat ID. Copy the Bot Token & Chat ID you received to `creds.ini` (remove [SAMPLE] from the name) file under `API_TOKEN` & `CHAT_ID` respectively. You're all set!

# Usage

**NOTE:** If adding this script to your environment variables, edit [line 9](https://github.com/ArionMiles/Filebot-To-Telegram/blob/master/telegram.py#L9), `'creds.ini'` to its absolute path (e.g: C:\Docs\User\creds.ini)

## telegram.py
#### Syntax:
`> telegram.py -t "TITLE" [-m "MESSAGE"]`

#### Example:
`> telegram.py -t "The Flash (2014)" -m "S03E15 - The Wrath of Savitar is ready."`

## telegraph_post.py
#### Syntax:
`> telegraph_post.py -t "TITLE" -c "CONTENT"`
Mainly made for use by Notifications_Processor in my Torrent Automation setup to submit a list of files processed.

----

Here's the config I use for my setup:
```
echo {quote("$n")} | Out-File -Encoding UTF8 SeriesName.txt; echo {quote("<b>${any{episode; s00e00 + ' - ' + t}{movie}}</b>")} | Out-File -Encoding UTF8 EpisodeDet.txt -append
```

You can put the above string in a text file and call it after execution of your AMC script by adding:
`--def exec="@path/to/args.txt"` to the script you add to Torrent client's *Execute after torrent completion* script.

This writes the name of the Series and Episodes processed to two files: `SeriesName` and `EpisodeDet.txt` respectively. Then, `Notification_Processor` checks whether the file `EpisodeDet.txt` contains more than 1 episode, and if it does, submits them to telegra.ph and sends the link to Telegram via bot. If it doesn't, then it sends the Name and Episode details to Telegram in text format via bot.

## Common Issues:

If you're on Windows and cannot run the telegram script from the command line after adding it to env. variables, do the following:

Regedit > `HKEY_CLASSES_ROOT\Applications\python27.exe\shell\open\command`
   
And change the value from : `"C:\Python27\python.exe" "%1"`
   
To: `"C:\Python27\python.exe" "%1" %*`

Similarly, set `HKEY_CLASSES_ROOT\py_auto_file\shell\open\command` to the same value. 

**adjust the path to your specific Python version.**

Read more about this [here.](http://eli.thegreenplace.net/2010/12/14/problem-passing-arguments-to-python-scripts-on-windows/)

# License
MIT License

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
