import os,time,logging,re

logging.basicConfig(filename='main.log',level=logging.INFO)
logging.info('start main.py')

from slackclient import SlackClient
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
    pattern=['sudo','Add files via upload']
    for pat in pattern:
        if re.match(pat,d.get('text')):
            sc.api_call(
                'chat.postMessage',
                channel=d['channel'],
                text=pat+' : '+d.get('text'))
            return None
    sc.api_call(
        'chat.postMessage',
        channel=d['channel'],
        text='pattern not found',
        thread_ts=d.get('ts'))


if sc.rtm_connect(with_team_state=True):
    while True:
        data=sc.rtm_read()
        if data == []:
            pass
        else:
            for d in data:
                print(d)
                if d['type'] == 'message' and d.get('subtype') is None:
                    if d.get('username') is 'sakakendobot' :
                        print('this is bot message')
                    else:
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
