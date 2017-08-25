import argparse
from telegram import telegram
from telegraph import Telegraph

__author__ = 'Kanishk Singh (Arion Miles)'
__license__ = "MIT"

PARSER = argparse.ArgumentParser(description="Telegra.ph submitter")
PARSER.add_argument('-title', '-t', type=str, help="Post title", required=False)
PARSER.add_argument('-content', '-c', type=str, nargs='*', help="Post content", required=False)
ARGS = PARSER.parse_args()

def telegraph_submit(message_title, message_content):
    title = message_title
    content = message_content
    telegraph = Telegraph()
    telegraph.create_account(short_name='FileBot')
    response = telegraph.create_page(title, html_content=content)
    posted = 'http://telegra.ph/{}'.format(response['path'])
    telegram(title, posted)

if __name__ == '__main__':
    title = ARGS.title
    content = ARGS.content
    telegraph = Telegraph()
    telegraph.create_account(short_name='FileBot')
    response = telegraph.create_page(title, html_content=content)
    posted = 'http://telegra.ph/{}'.format(response['path'])
    print posted
