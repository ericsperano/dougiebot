import os, time
from slackclient import SlackClient

READ_WEBSOCKET_DELAY = 1

def last_word(text):
    tokens = text.split(' ')
    while len(tokens) > 0:
        token = tokens.pop()
        if len(token) > 0 and token[0].isalpha():
            return ''.join(filter(str.isalnum, str(token)))

    return None

def main():
    BOT_ID = os.environ.get("BOT_ID")
    AT_BOT = "<@" + BOT_ID + ">"
    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    def parse_slack_output(slack_rtm_output):
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and AT_BOT in output['text']:
                    print("Someone told me:", output['text'])
                    return output['text'], output['channel']
        return None, None

    def repeat_last_word(text, channel):
        word = last_word(text.replace(AT_BOT, ''))
        if word:
            print("Repeating:", word)
            slack_client.api_call("chat.postMessage", channel=channel, text=word, as_user=True)

    if slack_client.rtm_connect():
        print("DougieBot connected and running!")
        while True:
            text, channel = parse_slack_output(slack_client.rtm_read())
            if text and channel:
                repeat_last_word(text, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
