from slackclient import SlackClient
import os,time

slack_token=os.getenv('SLACK_TOKEN_TEAMET')
sc=SlackClient(slack_token)

sudo=""
"\n"
"We trust you have received the usual lecture from the local System\n"
"Administrator. It usually boils down to these three things:\n"
"\n"
"    #1) Respect the privacy of others.\n"
"    #2) Think before you type.\n"
"    #3) With great power comes great responsibility.\n"
"\n"
""

def reply(d):
    if 'sudo' == d.get('text'):
        sc.api_call(
                'chat.postMessage',
                channel=d['channel'],
                text='sudo'+sudo)
#                thread_ts=d['ts'])
    elif 'Add files' in d['text']:
        sc.api_call(
                'chat.postMessage',
                channel=d['channel'],
                text='found Add files',
                thread_ts=d['ts'])
    else:
        sc.api_call(
                'chat.postMessage',
                channel=d['channel'],
                text='default reply. message is '+d['text'],
                thread_ts=d['ts'])




if sc.rtm_connect(with_team_state=True):
    while True:
        data=sc.rtm_read()
        if data == []:
            pass
        else:
            for d in data:
                print(d)
                if d['type'] == 'message' and d.get('subtype') is None:
                    #when message is simple message
                    if d.get('username') is 'sakakendobot' :
                        #when message is not bot-self
                        print('this is bot message')
                    else:
                        #wehn message is simpe and not by bot-self.reply
                        print('reply to thread',d['type'],d['ts'])
                        reply(d)
                elif d['type'] == 'hello':
                    sc.api_call(
                            'chat.postMessage',
                            channel='dev',
                            text='bot added')
        time.sleep(1)
else:
    print('Connection Failed')
