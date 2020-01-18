class Forward:
    def send_msg(self, app, line, message, message_id):
        app.forward_messages(line.id, message.chat.id, message_id)
            
class Copy:
    def send_msg(self, app, line, message, message_id):
        app.forward_messages(line.id, message.chat.id, message_id, 
            as_copy=True, remove_caption=True) 

def spam(app, line, message, message_id, spam_chan, trigger):
    print('Забракован пост из канала ', message.chat.title , ', для ленты ', line.name,', по триггеру ', trigger)
    app.forward_messages(spam_chan, message.chat.id, message_id) 

def send(app, message, message_id, line, spam_chan):
    
    if line.settings['filter']:
        if message.via_bot:
            spam(app, line, message, message_id, spam_chan, 'via_bot')
            return False
        else:
            filtering = ['t.me', 'vdutik', 'come in here', 'rvdm', 'add your channel', 
            'anime promotion', 'animepromotion', 'animedia', 'best channels', ''
            'сиськи админши', 'ваша админша', 'фулл', 'сочный слив', 'не заходить', '#реклама',
            'только у нас', 'все подробности тут', 'на этом канале', 'жуткое видео', 'подписывайтесь', 
            'подписывайся', 'ссылка на канал', 'хочу порекомендовать', 'подпишись', 'наши преимущества', 
            'думаешь над', 'только у нас', 'обращайтесь', 'за подробностями', 'заходите', 'переходи',
            'впустим', 'сохраняйте контакт']

            msg_txt_sm = str(message.caption).lower() if message.caption else str(message.text).lower()
            for i in filtering:
                if i in msg_txt_sm:
                    spam(app, line, message, message_id, spam_chan, i)
                    return False

    send = Copy() if line.settings['copy'] else Forward()

    if (line.settings['text'] and line.settings['sticker']):
        #text on, stick on. forward
        send.send_msg(app, line, message, message_id)
    elif line.settings['text']: 
        #text on, stick off, forward
        if message.sticker: return False
        else: send.send_msg(app, line, message, message_id)
    elif line.settings['sticker']:
        #text off, stick on, caption in media - ok, only plain text would be blocked
        if message.text:    return False
        else: send.send_msg(app, line, message, message_id)
    else:
        #text off/stiker off, forward media messages
        if   message.sticker: return False
        elif message.text:    return False
        else: send.send_msg(app, line, message, message_id)



