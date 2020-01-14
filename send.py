class All:
    #text on/stick on
    def send(self, app, message, msg_txt, line_id):
        app.forward_messages(line_id, message.chat.id, message.message_id) 

class AllFilt:
    #text on/stick on
    def send(self, app, message, msg_txt, line_id):
        for i in filtering:
            if i in (message.text).lower():
                return False
        app.forward_messages(line_id, message.chat.id, message.message_id) 

class WOStickFilt:
    #text on/stick off
    def send(self, app, message, msg_txt, line_id):
        for i in filtering:
            if i in (message.text).lower():
                return False
        if message.sticker: return False
        else: app.forward_messages(line_id, message.chat.id, message.message_id) 

class WOStick:
    #text on/stick off
    def send(self, app, message, msg_txt, line_id):
        if message.sticker: return False
        else: app.forward_messages(line_id, message.chat.id, message.message_id) 

class WOText:
    #text off/stick on
    def send(self, app, message, msg_txt, line_id):
        if message.text:    return False
        else: app.forward_messages(line_id, message.chat.id, message.message_id) 

class MedOnly:
    #text off/stiker off
    def send(self, app, message, msg_txt, line_id):
        if   message.sticker: return False
        elif message.text:    return False
        else: app.forward_messages(line_id, message.chat.id, message.message_id, 
                as_copy=True, remove_caption=True) 


filtering = [
    't.me', 'vdutik', 'come in here', 'rvdm', 'add your channel', 
    'сиськи админши', 'ваша админша', 'фулл', 'сочный слив', 'не заходить', '#реклама',
    'только у нас', 'все подробности тут', 'на этом канале', 'жуткое видео', 'подписывайтесь',
    'ссылка на канал', 'хочу порекомендовать'
]