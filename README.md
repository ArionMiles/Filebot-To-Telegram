# Telegram Bot for File Bot
Author: Arion_Miles

# Introduction
The bot is used in conjunction with a Automated Media Center, for example, my own setup consisting of Filebot (AMC Script), qBittorrent, and RSS Feeds to automatically send reports via push notifications on what content has been downloaded on to my Media Center, to my Phone.


# Motivation
By default, Filebot's AMC script provides a Pushbullet feature which sends a pushbullet notifications with a HTML documents of the files processed, and the title of the Pushbullet is the torrent's name. I needed something more concise, and the amount of text that can fit into a push notification and not require me to see the HTML doc along with it to see the files processed.

# Installation
Send a message to [@Filebot\_bot](https://t.me/Filebot_bot) on Telegram to start conversation, introduce yourself (say hello). Send command `/chatid` and it replies with a numerical string. Copy the Chat ID you received to `creds.ini` file under `CHAT_ID`. You're all set!

# Usage

**NOTE:** If adding this script to your environment variables, edit [line 9](https://github.com/ArionMiles/Filebot-To-Telegram/blob/master/telegram.py#L9), `'creds.ini'` to its absolute path (e.g: C:\Docs\User\creds.ini)

## Syntax:
`> telegram.py -t "TITLE" [-m "MESSAGE"]`

## Example:
`> telegram.py -t "The Flash (2014)" -m "S03E15 - The Wrath of Savitar is ready."`

Here's the config I use for my setup:
`telegram.py -t "*{movie}{episode; n}*" -m "{movie; 'The movie'}_{episode; s00e00}{episode; ' - '}{episode; t}_ is ready."`
Note that the asterisks (*) and underscores (_) are for Bold and Italic respectively.

You can put the above string in a text file and call it after execution of your AMC script by adding:
`--def exec="@path/to/args.txt"` to the script you add to Torrent client's *Execute after torrent completion* script.

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
