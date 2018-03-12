import os,time,logging,re

logging.basicConfig(filename='info.log',level=logging.INFO)
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

def id2name(d):
#    print('id2name',d)#,split(uid)[0])
    if d.get('user'):
        ret=sc.api_call('users.info',user=d.get('user'))
        logging.info('this is user'+ret.get('user').get('name'))
        return ret.get('user').get('name')
    elif d.get('bot_id'):
        ret=sc.api_call('bots.info',bot=d.get('bot_id'))
        logging.info('this is bot'+ret.egt("bot").get("name"))
        return ret.egt("bot").get("name")
    return None

def extract(d):
    attach=d.get('attachments')
    if attach is not None and len(attach) > 0 : text=attach[0].get('text')
    print(text)
    return text

def reply(d):
#    print('reply',d)
    print('name : ',id2name(d))
    if id2name(d) == 'github':
        if extract(d) is not None and re.search('Add files via upload',extract(d)):
            sc.api_call('chat.postMessage',channel=d.get('channel'),text='you should change commit message')

            

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
                        reply(d)
                elif d['type'] == 'hello':
                    sc.api_call(
                            'chat.postMessage',
                            channel='dev',
                            text='bot added')
        time.sleep(1)
else:
    print('Connection Failed')
