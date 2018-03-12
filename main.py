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

#def commit2filename(

def id2name(d):
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
    return text

def reply(d):
    last=[None for i in range(3)]
    print('name : ',id2name(d))
    if id2name(d) == 'github':
        text=extract(d)
        if text is not None and re.search('Add files via upload',text):
            sc.api_call('chat.postMessage',channel=d.get('channel'),text='you should specific commit message',thread_ts=d.get('ts'))
            for txt in re.split('[/\|:]',text) :
                if last[:0] == 'commit' : print('commit',last[-3:-2],last[:0])
                elif last[:0]=='compare': print('comp',last)#comp=txt
                last.append(txt)
                '''
                last[2]=last[1]
                last[1]=last[0]
                last[0]=txt
                '''
#print('comp,comm:',comp,comm)


def main():
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

if __name__ == '__main__':
    main()
